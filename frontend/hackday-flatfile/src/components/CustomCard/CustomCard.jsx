import React from 'react'
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'

const CustomCard = ({image}) => {

  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={image} height={180}/>
      <Card.Body>
        <Card.Title>Brand Threshold</Card.Title>
        <Card.Text>
          Upload a brand threshold CSV to flatfile
        </Card.Text>
        <Button variant="primary">Upload</Button>
      </Card.Body>
    </Card>
  )
}

export default CustomCard