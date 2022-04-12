import PropTypes, { InferProps } from 'prop-types';

import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

const CustomCard: any = ({ title, description, image, openFlatfile, type }: InferProps<typeof CustomCard.propTypes>) => {

  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={image} height={180}/>
      <Card.Body>
        <Card.Title>{title}</Card.Title>
        <Card.Text>
          {description}
        </Card.Text>
        <Button variant="primary" onClick={()=>openFlatfile(type)}>Upload</Button>
      </Card.Body>
    </Card>
  )
}

CustomCard.propTypes = {
  title: PropTypes.string,
  description: PropTypes.string,
  image: PropTypes.any,
  flatFileImporter: PropTypes.any,
  type: PropTypes.string
};

export default CustomCard