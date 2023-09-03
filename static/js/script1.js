// $(function() {
//   $.fn.liScroll = function(settings) {
//     settings = $.extend({
//       travelocity: 0.03,
//       pauseOnHover: true
//     }, settings);

//     return this.each(function() {
//       var $strip = $(this);
//       $strip.addClass("newsticker");
//       var stripHeight = 0;
//       $strip.find("li").each(function(i) {
//         stripHeight += $(this).outerHeight(true);
//       });

//       var $mask = $strip.wrap("<div class='mask'></div>");
//       var $tickercontainer = $strip.parent().wrap("<div class='tickercontainer'></div>");
//       var containerHeight = $strip.parent().parent().height();
//       $strip.height(stripHeight);
//       var totalTravel = stripHeight;
//       var defTiming = totalTravel / settings.travelocity;

//       function scrollNews(spazio, tempo) {
//         $strip.animate(
//           { top: '-=' + spazio },
//           tempo,
//           "linear",
//           function() {
//             if (parseInt($strip.css("top")) < -stripHeight) {
//               $strip.css("top", containerHeight);
//             }
//           }
//         );
//       }

//       scrollNews(totalTravel, defTiming);

//       // Trigger continuous scrolling
//       var timer = setInterval(function() {
//         scrollNews(totalTravel, defTiming);
//       }, 100);

//       // Pause scrolling on hover
//       if (settings.pauseOnHover) {
//         $strip.hover(
//           function() {
//             clearInterval(timer);
//           },
//           function() {
//             timer = setInterval(function() {
//               scrollNews(totalTravel, defTiming);
//             }, 100);
//           }
//         );
//       }
//     });
//   };

//   $("ul#ticker01").liScroll();
// });
$(document).ready(function() {
  $.fn.liScroll = function(settings) {
    settings = $.extend({
      travelocity: 0.03,
      pauseOnHover: true
    }, settings);

    return this.each(function() {
      var $strip = $(this);
      $strip.addClass("newsticker");
      var stripHeight = 0;
      $strip.find("li").each(function(i) {
        stripHeight += $(this).outerHeight(true);
      });

      var $mask = $strip.wrap("<div class='mask'></div>");
      var $tickercontainer = $strip.parent().wrap("<div class='tickercontainer'></div>");
      var containerHeight = $strip.parent().parent().height();
      $strip.height(stripHeight);
      var totalTravel = stripHeight;
      var defTiming = totalTravel / settings.travelocity;

      function scrollNews(spazio, tempo) {
        $strip.animate(
          { top: '-=' + spazio },
          tempo,
          "linear",
          function() {
            if (parseInt($strip.css("top")) < -stripHeight) {
              $strip.css("top", containerHeight);
            }
          }
        );
      }

      // Trigger continuous scrolling
      scrollNews(totalTravel, defTiming);

      // Pause scrolling on hover
      if (settings.pauseOnHover) {
        $strip.hover(
          function() {
            $strip.stop();
          },
          function() {
            scrollNews(totalTravel, defTiming);
          }
        );
      }
    });
  };

  $("div#ticker-container").liScroll();
});
