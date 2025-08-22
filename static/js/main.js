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
import { CalendarArrowDown } from "lucide";
import { CalendarArrowUp } from "lucide";

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
  CalendarArrowDown,
  CalendarArrowUp,
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
      CalendarArrowDown,
      CalendarArrowUp,
    },
  });
});
