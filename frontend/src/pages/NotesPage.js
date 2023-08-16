import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import ArrowBackIosNewIcon from "@mui/icons-material/ArrowBackIosNew";
// import jQuery from "jquery";

const NotesPage = () => {
  const params = useParams();
  const noteId = params.id;
 

  const navigate = useNavigate();

  const [note, setNote] = useState(null);

  useEffect(() => {
    getNote();
  }, [noteId]);

  const getNote = async () => {
    if (noteId === "new") return; // If new note
    const resp = await fetch(`/api/notes/${noteId}`);
    const data = await resp.json();
    console.log(data);
    setNote(data);
  };

  const updateNote = async () => {
    // var csrftoken = getCookie("csrftoken");
    fetch(`/api/notes/${noteId}/update/`, {
      // fetch(`/api/notes/${noteId}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        // "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(note),
    });
  };

  const createNote = async () => {
    // var csrftoken = getCookie("csrftoken");
    fetch(`/api/notes/create/`, {
      // fetch(`/api/notes/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(note),
    });
  };

  const deleteNote = async () => {
    // var csrftoken = getCookie("csrftoken");
    fetch(`/api/notes/${noteId}/delete/`, {
      // fetch(`/api/notes/${noteId}/`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        // "X-CSRFToken": csrftoken,
      },
    });
    navigate("/");
  };

  // function getCookie(name) {
  //   var cookieValue = null;
  //   if (document.cookie && document.cookie !== "") {
  //     var cookies = document.cookie.split(";");
  //     for (var i = 0; i < cookies.length; i++) {
  //       var cookie = jQuery.trim(cookies[i]);
  //       // Does this cookie string begin with the name we want?
  //       if (cookie.substring(0, name.length + 1) === name + "=") {
  //         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
  //         break;
  //       }
  //     }
  //   }
  //   return cookieValue;
  // }

  const handleSubmit = () => {
    if (noteId !== "new" && note.body === "") {
      deleteNote();
    } else if (noteId !== "new") {
      updateNote();
    } else if (noteId === "new" && note.body !== null) {
      createNote();
    }
    navigate("/");
  };

  const handleChange = (value) => {
    setNote({ ...note, body: value });
  };
  return (
    <div className="note">
      <div className="note-header">
        <ArrowBackIosNewIcon onClick={handleSubmit} />
        {noteId !== "new" ? (
          <button onClick={deleteNote}>Delete</button>
        ) : (
          <button onClick={handleSubmit}>Done</button>
        )}
      </div>

      <textarea
        onChange={(e) => handleChange(e.target.value)}
        value={note?.body}
      ></textarea>
    </div>
  );
};

export default NotesPage;
