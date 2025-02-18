import { useState } from "react";
import axios from "axios";
import "../styles/uploadform.css";

export default function UploadForm() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [image, setImage] = useState(null);
  const [markdown, setMarkdown] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (e, setFile) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title || !description || !image) {
      setMessage("Title, description, and image are required.");
      return;
    }

    const formData = new FormData();
    formData.append("title", title);
    formData.append("description", description);
    formData.append("image", image);
    if (markdown) formData.append("markdown", markdown);

    try {
      const response = await axios.post("/api/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage(error.response?.data?.error || "Upload failed");
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload Art File</h2>
      {message && <p className="message">{message}</p>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Title</label>
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required />
        </div>

        <div className="form-group">
          <label>Description</label>
          <textarea value={description} onChange={(e) => setDescription(e.target.value)} required></textarea>
        </div>

        <div className="form-group">
          <label>Image (png, jpg, jpeg, gif)</label>
          <input type="file" accept="image/*" onChange={(e) => handleFileChange(e, setImage)} required />
        </div>

        <div className="form-group">
          <label>Markdown File (Optional)</label>
          <input type="file" accept=".md" onChange={(e) => handleFileChange(e, setMarkdown)} />
        </div>

        <button type="submit" className="upload-button">Upload</button>
      </form>
    </div>
  );
}
