import React from "react";
import { Routes, Route } from "react-router-dom";
import NavBar from "./components/navbar.jsx";
import HomePage from "./pages/homepage.jsx";
import UploadForm from "./pages/uploadpage.jsx";

function App() {
    return (
        <div>
            <Routes> 
                <Route path="/" element={<HomePage />} />
                <Route path="/upload" element={<UploadForm />} />
            </Routes>
        </div>
        
    );
}

export default App;
