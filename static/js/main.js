import "vite/modulepreload-polyfill";
import "../css/main.css";

import { createIcons, Menu, ArrowRight, Globe } from "lucide";

createIcons({
  icons: {
    Menu,
    ArrowRight,
    Globe,
  },
});

console.log("sup");
