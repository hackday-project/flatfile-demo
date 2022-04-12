import { useEffect, useState, useRef } from 'react';
import Navbar from '../components/Navbar/Navbar';
import CustomCard from '../components/CustomCard/CustomCard';
import { flatfileImporter } from "@flatfile/sdk";

import './Loader.css';
import brand from '../assets/brand.webp';

const brandDescription = "Upload a brand threshold CSV to Flatfile"
const itemDescription = "Upload an item CSV to Flatfile"

const Loader = () => {
  const isInitialMount = useRef(true); // Keep track of when the inital render happens
  const [type, setType] = useState(""); 
  const [token, setToken] = useState(""); // JWT token

  const typeRef = useRef(type); // Create mutable object from the type state

  useEffect(() => {
    typeRef.current = type;
  });

  useEffect(() => {
    // Do nothing on initial render
    if (isInitialMount.current) {
      isInitialMount.current = false;
      return;
    }
    // Do not re-run once token has been cleared
    if (!token) {
      console.log("Importer closed, Token Cleared");
      return;
    }

    // Get the importer from the SDK using the JWT token
    let importer = flatfileImporter(token);

    // Setup subscriptions for the importer to hook on the flatfile event triggers
    importer.on('init', ({ batchId }) => { // On initialize, a unique batchId associated with the upload is created
      console.log(`Batch ${batchId} has been initialized.`);
    })
    importer.on("error", (error) => { // If any error occurs during uploading
      console.error(error);
    });
    importer.on("close", () => { // Once closed, via completion or exiting early. Reset the JWT token
      setToken("");
    });
    importer.on("complete", async ({ batchId }) => { // On complete, use the returned batchId to query the Django API to get the entries from the 
                                                     // batch and upload them to the DB. (Subscriptions are closed on complete)
      let url = ""
      if (typeRef.current === "brand") {
        url = "http://localhost:8000/loaderapp/trigger-brand";
      } else if (typeRef.current === "item") { 
        url = "http://localhost:8000/loaderapp/trigger-item";
      } else {
        return;
      }
      
      let data = JSON.stringify({batch_id: batchId});
      let response = await fetch(url, {
        mode: 'cors',
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: data
      });

      console.log(response);
      setToken("");
    });

    importer.launch();
  }, [token]);


  const openFlatfile = async (type: String): Promise<any> => {

    if (type.toLowerCase() === "item") {
      setToken("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWJlZCI6ImFjZjkxNTk1LTQ3NmItNDMzOC05ZTdlLTA2MjFiN2M0OWQwMSIsInN1YiI6InRlc3QifQ.GBeL0pnF4HivxQp9WGSJA4usv_zx8yUVFydCd4F2cJE");
    } else if (type.toLowerCase() === "brand") {
      setToken("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWJlZCI6Ijg5N2IyYzhiLTEyM2UtNDI4Yy1hNTFkLTM1NGI5YjgzNDQyNiIsInN1YiI6InRlc3QifQ.mjwbzM1ec_YHkeVQlnP9ZkrFwmZPjY8TO_7YiLUK7no");
    }

    // let request_body = JSON.stringify({
    //   user_id: "test",
    //   type: type.toLowerCase()
    // });

    // let response: any = await fetch("http://localhost:8000/loaderapp/embed-token", {
    //   mode: 'cors',
    //   method: 'POST',
    //   headers: {'Content-Type':'application/json'},
    //   body: request_body
    // })
    // response = await response.json();
    // let token = response.token;
    // console.log(token);
    
    if (type.toLowerCase() === "item") {
      setType("item");
    } else if (type.toLowerCase() === "brand") {
      setType("brand");
    }
  }


  return (
    <div className='loader-container'>
      <Navbar/>
      <div className='cards-container'>
        <CustomCard 
          title="Brand" 
          description={brandDescription} 
          image={brand}
          openFlatfile={openFlatfile}  
          type="brand"
        />
        <CustomCard 
          title="Item" 
          description={itemDescription} 
          image={brand}
          openFlatfile={openFlatfile}  
          type="item"
        />
      </div>
    </div>
  )
}

export default Loader