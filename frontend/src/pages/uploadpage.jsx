import { useState } from "react";
import axios from "axios";

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
    <div style={{ maxWidth: "500px", margin: "0 auto", padding: "20px", border: "1px solid #ccc", borderRadius: "5px", boxShadow: "2px 2px 12px rgba(0,0,0,0.1)" }}>
      <h2>Upload Art File</h2>
      {message && <p style={{ color: "red" }}>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: "10px" }}>
          <label>Title</label>
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required style={{ width: "100%", padding: "8px" }} />
        </div>

        <div style={{ marginBottom: "10px" }}>
          <label>Description</label>
          <textarea value={description} onChange={(e) => setDescription(e.target.value)} required style={{ width: "100%", padding: "8px" }}></textarea>
        </div>

        <div style={{ marginBottom: "10px" }}>
          <label>Image (png, jpg, jpeg, gif)</label>
          <input type="file" accept="image/*" onChange={(e) => handleFileChange(e, setImage)} required style={{ width: "100%", padding: "8px" }} />
        </div>

        <div style={{ marginBottom: "10px" }}>
          <label>Markdown File (Optional)</label>
          <input type="file" accept=".md" onChange={(e) => handleFileChange(e, setMarkdown)} style={{ width: "100%", padding: "8px" }} />
        </div>

        <button type="submit" style={{ width: "100%", padding: "10px", backgroundColor: "#007bff", color: "#fff", border: "none", cursor: "pointer" }}>Upload</button>
      </form>
    </div>
  );
}
