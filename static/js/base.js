// Script to make the sidebar visible on mobile devices

$(document).ready(function() {
    $("#sidebarCollapse").on("click", function() {
      $("#sidebar").addClass("active");
    });
  
    $("#sidebarCollapseX").on("click", function() {
      $("#sidebar").removeClass("active");
    });
  
    $("#sidebarCollapse").on("click", function() {
      if ($("#sidebar").hasClass("active")) {
        $(".overlay").addClass("visible");
      }
    });
  
    $("#sidebarCollapseX").on("click", function() {
      $(".overlay").removeClass("visible");
    });

    $(".jumbotron").css({ height: $(window).height() + "px" });

    $(window).on("resize", function() {
      $(".jumbotron").css({ height: $(window).height() + "px" });
    });
    
  });
  
