import React from "react";
import { Link } from "react-router-dom";
import AddIcon from "@mui/icons-material/Add";

const AddButton = () => {
  return (
    <>
      <Link to={"/note/new"} className="floating-button">
        <AddIcon />
      </Link>
    </>
  );
};

export default AddButton;
