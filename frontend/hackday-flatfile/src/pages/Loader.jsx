import { useEffect } from 'react';
import Navbar from '../components/Navbar/Navbar';
import CustomCard from '../components/CustomCard/CustomCard';

import './Loader.css';
import brand from '../assets/brand.webp';
import category from '../assets/category.jpeg';

const Loader = () => {
  const brandDescription = "Upload a brand threshold CSV to Flatfile"
  const categoryDescription = "Upload a category threshold CSV to Flatfile"

  useEffect(() => {
    let url = "http://localhost:8000/loaderapp/trigger-brand";
    fetch(url, {
      crossDomain:true,
      method: 'GET',
      headers: {'Content-Type':'application/json'},
    }).then(response => console.log(response))
  }, []);


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