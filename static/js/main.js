import "vite/modulepreload-polyfill";
import "../css/main.css";
import Swal from "sweetalert2";

import {
  createIcons,
  Heart,
  Star,
  Trash2,
  Edit,
  Plus,
  BookOpen,
  ChevronRight,
  ChevronLeft,
  ChevronsRight,
  ChevronsLeft,
} from "lucide";
import { deleteNote, highlightNote } from "./notes/notes";

window.Swal = Swal;
window.deleteNote = deleteNote;
window.highlightNote = highlightNote;
window.lucide = {
  createIcons,
  Heart,
  Star,
  Trash2,
  Edit,
  Plus,
  BookOpen,
  ChevronRight,
  ChevronLeft,
  ChevronsRight,
  ChevronsLeft,
};

document.addEventListener("DOMContentLoaded", () => {
  createIcons({
    icons: {
      Heart,
      Star,
      Trash2,
      Edit,
      Plus,
      BookOpen,
      ChevronRight,
      ChevronsRight,
      ChevronLeft,
      ChevronsLeft,
    },
  });
});
