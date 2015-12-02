// this is the production file (before collect-static)
(function( $ ){
  $.fn.pad = function( options, postDataCallback) {
    var settings = {
      'host'              : 'http://pad.open-academy.eu',
      'baseUrl'           : '/p/',
      'showControls'      : true,
      'showChat'          : false,
      'showLineNumbers'   : true,
      'userName'          : 'unnamed',
      'lang'              : '',
      'useMonospaceFont'  : false,
      'noColors'          : false,
      'userColor'         : false,
      'hideQRCode'        : false,
      'alwaysShowChat'    : false,
      'width'             : 100,
      'height'            : 600,
      'border'            : 0,
      'borderStyle'       : 'solid',
      'toggleTextOn'      : 'Disable Rich-text',
      'toggleTextOff'     : 'Enable Rich-text',
      'plugins'           : {},
      'rtl'               : false
    };
    
    var $self = this;
    // console.log('line 27', this.children().first().context.childNodes[1] ) //.filter('#chatbox'))
    if (!$self.length) return;
    if (!$self.attr('id')) throw new Error('No "id" attribute');
    
    var useValue = $self[0].tagName.toLowerCase() == 'textarea';
    var selfId = $self.attr('id');
    var epframeId = 'epframe'+ selfId;
    // This writes a new frame if required
    if ( !options.getContents ) {
      if ( options ) {
        $.extend( settings, options );
      }
      
      var pluginParams = '';
      for(var option in settings.plugins) {
        pluginParams += '&' + option + '=' + settings.plugins[option]
      }

      // iFrameLink is the link to the real etherpad:
      var iFrameLink = '<iframe id="'+epframeId; 
          iFrameLink = iFrameLink +'" name="' + epframeId;
          iFrameLink = iFrameLink +'" src="' + settings.host+settings.baseUrl+options.padId;
          iFrameLink = iFrameLink + '?showControls=' + settings.showControls;
          iFrameLink = iFrameLink + '&showChat=' + settings.showChat;
          iFrameLink = iFrameLink + '&showLineNumbers=' + settings.showLineNumbers;
          iFrameLink = iFrameLink + '&useMonospaceFont=' + settings.useMonospaceFont;
          iFrameLink = iFrameLink + '&userName=' + settings.userName;
          if (settings.lang) {
            iFrameLink = iFrameLink + '&lang=' + settings.lang;
          }
          iFrameLink = iFrameLink + '&noColors=' + settings.noColors;
          iFrameLink = iFrameLink + '&userColor=' + settings.userColor;
          iFrameLink = iFrameLink + '&hideQRCode=' + settings.hideQRCode;
          iFrameLink = iFrameLink + '&alwaysShowChat=' + settings.alwaysShowChat;
          iFrameLink = iFrameLink + '&rtl=' + settings.rtl;
          iFrameLink = iFrameLink + pluginParams;
          iFrameLink = iFrameLink +'" style="border:' + settings.border;
          iFrameLink = iFrameLink +'; border-style:' + settings.borderStyle;
          iFrameLink = iFrameLink +';" width="' + '100%';//settings.width;
          iFrameLink = iFrameLink +'" height="' + settings.height; 
          iFrameLink = iFrameLink +'"></iframe>';
      
      var $iFrameLink = $(iFrameLink);
      
      if (useValue) {
        var $toggleLink = $('<a href="#'+ selfId +'">'+ settings.toggleTextOn +'</a>').click(function(){
          var $this = $(this);
          $this.toggleClass('active');
          if ($this.hasClass('active')) $this.text(settings.toggleTextOff);
          $self.pad({getContents: true});
          return false;
        });
        $self
          .hide()
          .after($toggleLink)
          .after($iFrameLink)
        ;
      }
      else {      
        $self.html(iFrameLink);
      }
    }
    // This reads the etherpad contents if required
    else {
      var frameUrl = settings.host+settings.baseUrl+options.padId;
      var contentsUrl = frameUrl + "/export/html";
      var target = $('#'+ options.getContents);
      // perform an ajax call on contentsUrl and write it to the parent
      $.get(contentsUrl, function(data) {
        // console.log('data', data)
        heading = data.split("</h1>")[1] + "</h1>" 
        textbody= data.split("</h1>")[2]
        data = heading + textbody
        if (target.is(':input')) {
          target.val(data).show();
        }
        else {
          target.html(data);
        }
        postDataCallback(data)
        $('#'+ epframeId).remove();
      });
    }
    
    return $self;
  };
})( jQuery );
