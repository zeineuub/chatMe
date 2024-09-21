// NavBar.js
import React from 'react';
import Profile from './../Menu/Profile/Profile';
import SearchBar from './../SearchBar/SearchBar';
import logo from "../../assets/images/iconchatme.png";
const Navbar = () => {
  return (
    
    <nav className="navbar  fixed-top navbar-light" style={{backgroundColor: "#d2e9f4"}}>
        <a className="navbar-brand" href="#">
            <img src= {logo} width="40" height="40" alt="" className='mx-3'/>
        </a>

        <SearchBar />
        <Profile/>
    </nav>
  );
};

export default Navbar;
