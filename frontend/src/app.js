import React from "react";
import { Routes, Route } from "react-router-dom";
import NavBar from "./components/navbar.jsx";
import HomePage from "./pages/homepage.jsx";
import UploadForm from "./pages/uploadpage.jsx";
import ArtPage from "./pages/artpage.jsx";    


function App() {
    return (
        <div>
            <NavBar />
            <Routes> 
                <Route path="/" element={<HomePage />} />
                <Route path="/upload" element={<UploadForm />} />
                <Route path="/art/:id" element={<ArtPage />} />
            </Routes>
        </div>
        
    );
}

export default App;
