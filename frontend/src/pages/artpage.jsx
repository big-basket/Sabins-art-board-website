import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

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
    <div className="container mx-auto p-6">
      <h1 className="text-2xl font-bold">{artwork.title}</h1>
      <img
        src={artwork.image_filename}
        alt={artwork.title}
        className="w-full h-auto my-4"
      />
      <p className="text-gray-700">{artwork.description}</p>
    </div>
  );
};

export default ArtPage;
