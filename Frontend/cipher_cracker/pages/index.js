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
  const [alreadyBeenSubmit, setAlreadyBeenSubmit] = useState(false);
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
    setAlreadyBeenSubmit(true)
    
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
        const keyAsString = JSON.stringify(result.result.key)
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
          const keyAsString = JSON.stringify(result.key)
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
    const keyAsString = JSON.stringify(result.key)
    setKey(keyAsString)
  }

  return (
    <div>
      <Head>
        <title>Cipher Cracker</title>
      </Head>
      <div className={styles.container}>
        <NavBar></NavBar>


      <div className='mb-4'>
        <h1 className="display-4">Decrypter Tool</h1>
        <p className="lead">Use this tool to decrypt any Caesar, Transposition or Substitution cipher. For more information, please see the Encryption Methods page.</p>
      </div>

      <div className="d-flex flex-row justify-content-between">

        <div className="jumbotron" style={{width: "40%"}}>
          <h1 className="display-6">Query</h1>
          <hr className="my-4"></hr>
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="selectCipherType" className="form-label">Cipher Type:</label>
              <select className="form-select" name="cipherType" defaultValue="caesar" id="selectCipherType">
                <option value="caesar">Caesar</option>
                <option value="transposition">Transposition</option>
                <option value="substitution">Substitution</option>
                <option value="unknown">Unknown</option>
              </select>
              <div className="form-text">If the encryption method of the ciphertext is not known, use the unknown option.</div>
            </div>
            <div className="mb-3">
              <label htmlFor="cipherText" className="form-label">Ciphertext:</label>
              <textarea name="cipherText" id="cipherText" className="form-control" placeholder="Enter Ciphertext..." rows="9" />
            </div>
            <button type="submit" className="btn btn-primary btn-lg">Decrypt</button>
          </form>
        </div>

        <div style={{position: "relative", width: "15%"}}>
          <Image src="/arrow-right.svg" layout="fill" objectFit="contain"></Image>
        </div>
        

        <div className="jumbotron" style={{width: "40%"}}>
          <h1 className="display-6">Result</h1>
          <hr className="my-4"></hr>

          <form>
            <div className="mb-3">
            <label htmlFor="key" className="form-label">Key:</label>
            <textarea id="key" className="form-control" placeholder="Please enter valid ciphertext first..." value={key} rows="2" readOnly></textarea>
            </div>
            <div className="mb-3">
              <label htmlFor="plaintext" className="form-label">Plaintext:</label>
              <textarea id="plaintext" className="form-control" placeholder="Please enter valid ciphertext first..." value={plainText} rows="9" readOnly/>
            </div>
          </form>
          
          
          

          
          


          

          {alreadyBeenSubmit &&
            <div id='results-box'>
              {errorMessage ? (
                <div id='error-message-box'>
                  <h2>Error Message:</h2>
                  <p>{errorMessage}</p>
                </div>
              ) : ( 
                
                <div id='general-results-box'>
                  {unknownCipherType &&
                    <p> The plaintext for the ciphertext that you entered was encrypted using a <b>{unknownCipherType}</b> cipher. </p>
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
          }
          
        </div>


      </div>

      
      
      
      
      

        

        




        
      </div>
    </div>
  )
}