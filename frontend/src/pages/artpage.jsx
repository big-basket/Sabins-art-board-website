import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "../styles/artpage.css"; 

const ArtPage = () => {
  const { id } = useParams();
  const [artwork, setArtwork] = useState(null);

  useEffect(() => {
    fetch("/api/artpins")  
      .then((res) => res.json())
      .then((data) => {
        const foundArtwork = data.find((art) => art.id.toString() === id);
        setArtwork(foundArtwork);
      });
  }, [id]);

  if (!artwork) return <p>Loading...</p>;

  return (
    <div className="art-container">
      <h1 className="art-title">{artwork.title}</h1>
      <img
        src={artwork.image_filename}
        alt={artwork.title}
        className="art-image"
      />
      <p className="art-description">{artwork.description}</p>
    </div>
  );
};

export default ArtPage;
