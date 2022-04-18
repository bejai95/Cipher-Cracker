import Head from 'next/head';
import Image from 'next/image';
import styles from '../styles/Home.module.css';
import apiurl from "../utils/apiurl";
import { useState, useEffect } from "react";
import NavBar from "../components/NavBar.js"

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
  const [isSubstitution, setIsSubstitution] = useState(false);


  async function handleSubmit(event) {
    event.preventDefault();
    
    setCipherText(event.target.cipherText.value);
    const cipherType = event.target.cipherType.value; // useState is asynchronous
    const apiurlFull = apiurl + cipherType;

    if (cipherType === "substitution") {
      setIsSubstitution(true)
      apiurlFull += "?mode=partial"
    } else {
      setIsSubstitution(false)
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
        setIsSubstitution(true)
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
    <div>
      <Head>
        <title>Cipher Cracker</title>
      </Head>
      <div className={styles.container}>
        <NavBar></NavBar>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label for="selectCipherType" className="form-label">Cipher Type:</label>
            <select className="form-select" name="cipherType" defaultValue="caesar" id="selectCipherType">
              <option value="caesar">Caesar</option>
              <option value="transposition">Transposition</option>
              <option value="substitution">Substitution</option>
              <option value="unknown">Unknown</option>
            </select>
            <div className="form-text">If the encryption method of the ciphertext is not known, use the unknown option.</div>
          </div>
          <div className="mb-3">
            <label for="cipherText" className="form-label">Ciphertext:</label>
            <textarea name="cipherText" id="cipherText" className="form-control" placeholder="Enter Ciphertext..." rows="10" />
          </div>
        
        
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        <div id='results-box'>
          {errorMessage ? (
            <div id='error-message-box'>
              <h2>Error Message:</h2>
              <p>{errorMessage}</p>
            </div>
          ) : ( 
            
            <div id='general-results-box'>
              {unknownCipherType &&
                <div id='unknown-cipher-type-box'>
                  <h2>Unknown Cipher Type:</h2>
                  <p>{unknownCipherType}</p>
                </div>
              }                  
              
              <h2>Plaintext:</h2>
              <NewlineText text={plainText} />
              <h2>Key:</h2>
              <p>{key}</p>

              {isSubstitution &&
                <div id='full-substitution-options-box'>
                  <h2>Total Amount Possibilities (for substitution):</h2>
                  <p>{totalAmountPossibilities}</p>
                  <h2>Full substitution option:</h2>
                  <button onClick={handleFullSubstitution}>Full Substitution</button>
                </div>
              }
            
            </div>
          )} 
        </div>
      </div>
    </div>
  )
}