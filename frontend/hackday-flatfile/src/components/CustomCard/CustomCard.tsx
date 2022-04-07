import PropTypes, { InferProps } from 'prop-types';



import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

import { flatfileImporter } from "@flatfile/sdk";

const embedId = "897b2c8b-123e-428c-a51d-354b9b834426";
const endUserEmail = "angusleung228@hotmail.com";
const privateKey = "WV5ups3cIjAkgmp6PdZsHwDUXuCXXe5N9y9yiGGSvahQewRV1c0VJiTVI8L7H5YZ";

const CustomCard: any = ({ title, description, image}: InferProps<typeof CustomCard.propTypes>) => {

  const openFlatfile = async (): Promise<any> => {
    const importer = flatfileImporter("");

    await importer.__unsafeGenerateToken({
      privateKey: privateKey,
      embedId: embedId,
      endUserEmail: endUserEmail,
    });


    importer.launch();
  }


  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={image} height={180}/>
      <Card.Body>
        <Card.Title>{title}</Card.Title>
        <Card.Text>
          {description}
        </Card.Text>
        {/* <FlatfileButton
          licenseKey="e4e520f6-3026-432a-8ca3-49418bada848"
          customer={{
              companyId: "ABC-123",
              companyName: "ABC Corp.",
              email: "john@abc123.com",
              name: "John Smith",
              userId: "12345"
          }}
          settings={{
              type: "Brand Thresholds",
              fields: [
                  { label: "Version", key: "version" },
                  { label: "Minimum Threshold", key: "min_threshold" },
                  { label: "Brand Name", key: "key" }
              ],
              managed: true
          }}
          onData={async (results) => {
              // Do something with the data here
              console.log(results);
              return "Done!";
          }}
      >
        Upload
      </FlatfileButton> */}
        <Button variant="primary" onClick={() => openFlatfile()}>Upload</Button>
      </Card.Body>
    </Card>
  )
}

CustomCard.propTypes = {
  title: PropTypes.string,
  description: PropTypes.string,
  image: PropTypes.any
};

export default CustomCard