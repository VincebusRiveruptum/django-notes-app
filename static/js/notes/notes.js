import { RefreshCcw } from "lucide";
import Swal from "sweetalert2";
import { getCsrfToken } from "./csrf";

export const deleteNote = async (noteId, bookId) => {
  if (noteId && bookId) {
    const result = await Swal.fire({
      icon: "warning",
      title: "Delete note",
      text: "Are you sure?",
      showConfirmButton: true,
      showCancelButton: true,
    });

    if (result.isConfirmed) {
      const response = await fetch(`/books/${bookId}/notes/${noteId}/delete`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCsrfToken(),
        },
      });

      window.location.href = `/books/${bookId}/notes`;
    }
  } else {
    throw Error("Invalid note to remove.");
  }
};

export const highlightNote = async (noteId, bookId, currentValue) => {
  console.log(noteId, bookId);

  let value;

  if (currentValue) {
    value = false;
  } else {
    value = true;
  }

  try {
    const response = await fetch(`/books/${bookId}/notes/${noteId}/highlight`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCsrfToken(),
      },
      body: JSON.stringify({
        highlighted: true,
      }),
    });
  } catch (e) {
    console.error(e);
  }

  window.location.reload();
};
