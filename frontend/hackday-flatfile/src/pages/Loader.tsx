import { useEffect, useState } from 'react';
import Navbar from '../components/Navbar/Navbar';
import CustomCard from '../components/CustomCard/CustomCard';
import Button from 'react-bootstrap/Button';
import { flatfileImporter } from "@flatfile/sdk";

import './Loader.css';
import brand from '../assets/brand.webp';
// import category from '../assets/category.jpeg';

const importer = flatfileImporter("");
const embedId = "897b2c8b-123e-428c-a51d-354b9b834426";
const endUserEmail = "angusleung228@hotmail.com";
const privateKey = "WV5ups3cIjAkgmp6PdZsHwDUXuCXXe5N9y9yiGGSvahQewRV1c0VJiTVI8L7H5YZ";
const brandDescription = "Upload a brand threshold CSV to Flatfile"
const categoryDescription = "Upload a category threshold CSV to Flatfile"

const Loader = () => {
  const [batch_id, setBatchId] = useState('');

  useEffect(() => {
    importer.on('init', ({ batchId }) => {
      console.log(`Batch ${batchId} has been initialized.`);
      setBatchId(batchId);
    })
  
    importer.on("error", (error) => {
      console.error(error);
    });
    
    importer.on("complete", async (payload) => {
      console.log(JSON.stringify(await payload.data(), null, 2));
      let url = "http://localhost:8000/loaderapp/trigger-brand";
      if (batch_id) {
        let data = JSON.stringify(batch_id);
        console.log(data)
        fetch(url, {
          mode: 'cors',
          method: 'POST',
          headers: {'Content-Type':'application/json'},
          body: data
        }).then(response => console.log(response))
      }
    });
  }, []);

  const uploadCallback = async () => {
    if (batch_id) {
      let data = JSON.stringify({ batch_id: batch_id});
      let url = "http://localhost:8000/loaderapp/trigger-brand";
      console.log(data)
      
      fetch(url, {
        mode: 'cors',
        method: 'POST',
        headers: {
          'Content-Type':'application/json'
        },
        body: data
      }).then(response => console.log(response))
    }
  }

  const openFlatfile = async (): Promise<any> => {
    console.log("Here");
    await importer.__unsafeGenerateToken({
      privateKey: privateKey,
      embedId: embedId,
      endUserEmail: endUserEmail,
    });

    importer.launch();
  }


  return (
    <div className='loader-container'>
      <Navbar/>
      <div className='cards-container'>
        <CustomCard 
          title="Brand Thresholds" 
          description={brandDescription} 
          image={brand}
          openFlatfile={openFlatfile}  
        />
        <Button onClick={() => uploadCallback()}>Click</Button>
        {/* <CustomCard title="Category Thresholds" description={categoryDescription} image={category}/> */}
      </div>
    </div>
  )
}

export default Loader