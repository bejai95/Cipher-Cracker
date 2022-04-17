import Head from 'next/head';
import Image from 'next/image';
import styles from '../styles/Home.module.css';
import apiurl from "../utils/apiurl";
import { useState, useEffect } from "react";

function NewlineText(props) {
  const text = props.text;
  const newText = text.split('\n').map((str, index) => <p key={index}>{str}</p>);
  return newText;
}

export default function Home() {
  const [cipherText, setCipherText] = useState("");
  const [plainText, setPlainText] = useState("");
  const [key, setKey] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [unknownCipherType, setUnknownCipherType] = useState("");
  const [totalAmountPossibilities, setTotalAmountPossibilities] = useState("");
  const [intersectedMapping, setIntersectedMapping] = useState({});

  async function handleSubmit(event) {
    event.preventDefault();
    
    setCipherText(event.target.cipherText.value)
    const cipherType = event.target.cipherType.value; // Need to do it this way because useState is asynchronous
    const apiurlFull = apiurl + cipherType;

  if (cipherType === "substitution") {
    apiurlFull += "?mode=partial"
  }

    const res = await fetch(
      apiurlFull,
      {
        body: JSON.stringify({
          cipherText: event.target.cipherText.value
        }),
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'PUT'
      }
    )

    const result = await res.json()

    setErrorMessage("")
    setUnknownCipherType("")
    setTotalAmountPossibilities("")
    setIntersectedMapping({})

    if (cipherType === "unknown") {
      setUnknownCipherType(result.cipherType)
      setPlainText(result.result.plainText)

      if (result.cipherType === "substitution") {
        setTotalAmountPossibilities(result.result.totalAmountPossibilities)
        setIntersectedMapping(result.result.intersectedMapping)
        const keyAsString = JSON.stringify(result.result.key, null, 1)
        setKey(keyAsString)
      } else {
        setKey(result.result.key)
      }
      
    } else {
      if ("message" in result) {
        setPlainText("");
        setKey("");
        setErrorMessage(result.message)
      } else {
        setPlainText(result.plainText)
        
        if (cipherType === "substitution") {
          setTotalAmountPossibilities(result.totalAmountPossibilities)
          setIntersectedMapping(result.intersectedMapping)
          const keyAsString = JSON.stringify(result.key, null, 1)
          setKey(keyAsString)
        } else {
          setKey(result.key);
        }
      }
    }
  }

  async function handleFullSubstitution() {
    const res = await fetch(
      apiurl + 'substitution?mode=full',
      {
        body: JSON.stringify({
          cipherText: cipherText,
          intersectedMapping: intersectedMapping
        }),
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'PUT'
      }
    )
    const result = await res.json()

    setPlainText(result.plainText)
    const keyAsString = JSON.stringify(result.key, null, 1)
    setKey(keyAsString)
  }

  
  return (
    <div className={styles.container}>
      <Head>
        <title>Cipher Cracker</title>
      </Head>
      <div>
        <h1>Cipher Cracker</h1>
          <form onSubmit={handleSubmit}>
            <select name="cipherType" defaultValue="caesar">
              <option value="caesar">Caesar</option>
              <option value="transposition">Transposition</option>
              <option value="substitution">Substitution</option>
              <option value="unknown">Unknown</option>
            </select>
            <br></br>
            <br></br>
            <textarea name="cipherText" placeholder="Enter Ciphertext..." rows="20" cols="50" />
            <br></br>
            <button type="submit">Submit</button>
          </form>
          <h2>Plaintext:</h2>
          <NewlineText text={plainText} />
          <h2>Key:</h2>
          <p>{key}</p>
          <h2>Error Message:</h2>
          <p>{errorMessage}</p>
          <h2>Unknown Cipher Type:</h2>
          <p>{unknownCipherType}</p>
          <h2>Total Amount Possibilities (for substitution):</h2>
          <p>{totalAmountPossibilities}</p>
          <h2>Full substitution options:</h2>
          <button onClick={handleFullSubstitution}>Full Substitution</button>


      </div>
    </div>
  )
}