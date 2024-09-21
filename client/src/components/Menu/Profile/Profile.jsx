// Profile.js
import React, { useState,useEffect,useRef } from 'react';
import './Profile.css'; 
import {useAuth} from '../../../utils/AuthProvider';
import {useNavigate  } from 'react-router-dom';
import DropdownItem from './DropdownItem';
const Profile = () => {
  const [open, setOpen] = useState(false);
  const { logout } = useAuth();
  const navigate = useNavigate();
  let menuRef = useRef();
  const [user, setUser] = useState({});
  useEffect(() => {
    let handler = (e)=>{
      if(!menuRef.current.contains(e.target)){
        setOpen(false);
        console.log(menuRef.current);
      }      
    };
    setUser(JSON.parse(localStorage.getItem("user")));
    document.addEventListener("mousedown", handler);
    return() =>{
      document.removeEventListener("mousedown", handler);
    }
    
  });
  const handleSignOut = () => {
    console.log("User signed out");
    logout();
    navigate("/login");
  };
  return (
    <div className='menu-container' ref={menuRef}>
        <div className='menu-trigger' onClick={()=>{setOpen(!open)}}>
          
        </div>

        <div className={`dropdown-menu ${open? 'active' : 'inactive'}`} >
          <h3>{user.fullname}<br/><span>{user.email}</span></h3>
          <ul>
            
            <DropdownItem icon = "bi bi-person-circle" text = {"My Profile"}/>
            <DropdownItem icon = "bi bi-gear" text = {"Edit Profile"}/>
            <DropdownItem icon ="bi bi-sliders" text = {"Settings"}/>
            <DropdownItem icon =" bi bi-box-arrow-right" text = {"Logout"}/>
          </ul>
        </div>
      </div>
  );
};

export default Profile;
