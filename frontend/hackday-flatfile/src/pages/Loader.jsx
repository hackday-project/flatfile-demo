import React from 'react'
import Navbar from '../components/Navbar/Navbar';
import CustomCard from '../components/CustomCard/CustomCard';

import './Loader.css';
import brand from '../assets/brand.webp';
import category from '../assets/category.jpeg';

const Loader = () => {
  return (
    <div className='loader-container'>
      <Navbar/>
      <div className='cards-container'>
        <CustomCard image={brand}/>
        <CustomCard image={category}/>
      </div>
    </div>
  )
}

export default Loader