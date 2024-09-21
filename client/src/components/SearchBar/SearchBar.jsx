// SearchBar.js
import React from 'react';
import './SearchBar.css'; // Ensure you have this CSS file for custom styles

const SearchBar = () => {
  return (
    <div className="search-form">
      <i className="bi bi-search search-icon"></i>
      <input 
        className="form-control search-input"
        type="search" 
        placeholder="Search" 
        aria-label="Search" 
      />
    </div>
  );
};

export default SearchBar;
