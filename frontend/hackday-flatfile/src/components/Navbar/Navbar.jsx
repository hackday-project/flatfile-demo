import React from 'react';
import './Navbar.css';

import logo from '../../assets/Numerator_Logo.png';

const Navbar = () => {
  return (
    <div className='nav-container'>
      <img src={logo} alt="Numerator_logo" />
      <h1>Loader - Flatfile</h1>
    </div>
  )
}

export default Navbar