import React from 'react'
import { useRef, useState } from "react";
import PropTypes, { InferProps } from 'prop-types'

import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'
// import { FlatfileButton } from '@flatfile/react/src'


const embedId = "897b2c8b-123e-428c-a51d-354b9b834426";
const endUserEmail = "angusleung228@hotmail.com";
const privateKey = "WV5ups3cIjAkgmp6PdZsHwDUXuCXXe5N9y9yiGGSvahQewRV1c0VJiTVI8L7H5YZ";

const CustomCard: any = ({image}: InferProps<typeof CustomCard.propTypes>) => {

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

CustomCard.propTypes = {
  image: PropTypes.string
};

export default CustomCard