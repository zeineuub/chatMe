import React from 'react';
import './Profile.css'; 

const DropdownItem = ({ icon, text, onClick }) => {
  return (
    <li className='dropdownItem' onClick={onClick}>
      <i className={icon}></i>
      <a> {text} </a>
    </li>
  );
};

export default DropdownItem;
