import "vite/modulepreload-polyfill";
import "../css/main.css";
import Swal from "sweetalert2";

import { createIcons, Menu, ArrowRight, Globe } from "lucide";

import { deleteNote, highlightNote } from "./notes/notes";

window.Swal = Swal;
window.deleteNote = deleteNote;
window.highlightNote = highlightNote;

createIcons({
  icons: {
    Menu,
    ArrowRight,
    Globe,
  },
});
