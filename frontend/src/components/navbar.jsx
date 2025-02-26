import {Link } from "react-router-dom";
import React from "react";

export default function NavBar() {
    return (
        <div className="navbar">
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/upload">Upload</Link></li>
                </ul>
            </nav>
        </div>
    );
}
