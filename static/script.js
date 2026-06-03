//console.log("Script loading");
//document.writeln("Script is loaded");

document.addEventListener("DOMContentLoaded", () => {
      const typedElement = document.querySelector('.typed');
      if (typedElement) {
        let typed_strings = typedElement.getAttribute('data-typed-items');
        typed_strings = typed_strings.split(',').map(s => s.trim());

        new Typed('.typed', {
          strings: typed_strings,
          typeSpeed: 100,
          backSpeed: 50,
          backDelay: 2000,
          loop: true
        });
      }
});