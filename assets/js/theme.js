(function () {
  "use strict";

  var STORAGE_KEY = "fz-theme";
  var html = document.documentElement;
  var btn = document.getElementById("theme-toggle");
  if (!btn) return;

  function setTheme(t) {
    html.setAttribute("data-theme", t);
    try { localStorage.setItem(STORAGE_KEY, t); } catch (e) {}
  }

  btn.addEventListener("click", function () {
    var current = html.getAttribute("data-theme") || "dark";
    setTheme(current === "dark" ? "light" : "dark");
  });

  // Console love letter
  try {
    var msg = "%cIf you opened DevTools, you're probably interviewing me.";
    var sub = "Hire me: fzorrill@ethz.ch · linkedin.com/in/fzorrilla94";
    console.log(msg, "color:#7DD3A0;font-family:JetBrains Mono;font-size:14px;font-weight:bold");
    console.log(sub);
  } catch (e) {}
})();
