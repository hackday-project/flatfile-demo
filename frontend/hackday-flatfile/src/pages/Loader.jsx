import React from 'react'
import Navbar from '../components/Navbar/Navbar';
import CustomCard from '../components/CustomCard/CustomCard';

import './Loader.css';
import brand from '../assets/brand.webp';
import category from '../assets/category.jpeg';

const Loader = () => {
  const brandDescription = "Upload a brand threshold CSV to Flatfile"
  const categoryDescription = "Upload a category threshold CSV to Flatfile"

  return (
    <div className='loader-container'>
      <Navbar/>
      <div className='cards-container'>
        <CustomCard title="Brand Thresholds" description={brandDescription} image={brand}/>
        <CustomCard title="Category Thresholds" description={categoryDescription} image={category}/>
      </div>
    </div>
  )
}

export default Loader