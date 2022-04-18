import Head from 'next/head';
import Image from 'next/image';
import styles from '../styles/Home.module.css';
import apiurl from "../utils/apiurl";
import { useState } from "react";
import NavBar from "../components/NavBar.js"
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import CloseButton from 'react-bootstrap/CloseButton';

export default function Home() {
  const [alreadyBeenSubmit, setAlreadyBeenSubmit] = useState(false);

  const [cipherText, setCipherText] = useState("");
  const [plainText, setPlainText] = useState("");
  const [key, setKey] = useState("");

  const [showErrorModal, setShowErrorModal] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const [unknownCipherType, setUnknownCipherType] = useState("");
  
  const [showSubstitutionModal, setShowSubstitutionModal] = useState(false);
  const [totalAmountPossibilities, setTotalAmountPossibilities] = useState("");
  const [intersectedMapping, setIntersectedMapping] = useState({});

  async function handleSubmit(event) {
    event.preventDefault();
    setAlreadyBeenSubmit(true)
    
    setCipherText(event.target.cipherText.value);
    const cipherType = event.target.cipherType.value; // useState is asynchronous
    const apiurlFull = apiurl + cipherType;

    if (cipherType === "substitution") {
      setShowSubstitutionModal(true)
      apiurlFull += "?mode=partial"
    } else {
      setShowSubstitutionModal(false)
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
    setShowErrorModal(false)
    setUnknownCipherType("")
    setTotalAmountPossibilities("")
    setIntersectedMapping({})
    
    if (cipherType === "unknown") {
      setUnknownCipherType(result.cipherType)
      setPlainText(result.result.plainText)

      if (result.cipherType === "substitution") {
        setShowSubstitutionModal(true)
        
        let amountPossible = result.result.totalAmountPossibilities;
        if (amountPossible != 1) {
          setTotalAmountPossibilities(amountPossible)
        } else {
          setTotalAmountPossibilities("infinite")
        }
        
        setIntersectedMapping(result.result.intersectedMapping)
        const keyAsString = JSON.stringify(result.result.key)
        setKey(keyAsString);

      } else {
        setKey(result.result.key)
      }
      
    } else {
      if ("message" in result) {
        setPlainText("");
        setKey("");
        setErrorMessage(result.message)
        setShowErrorModal(true)
      } else {
        setPlainText(result.plainText)
        
        if (cipherType === "substitution") {
          let amountPossible = result.totalAmountPossibilities;
          if (amountPossible != 1) {
            setTotalAmountPossibilities(amountPossible)
          } else {
            setTotalAmountPossibilities("infinite")
          }
        
          setIntersectedMapping(result.intersectedMapping)
          const keyAsString = JSON.stringify(result.key)
          setKey(keyAsString)
        } else {
          setKey(result.key);
        }
      }
    }
  }

  function handleErrorModalClose() {
    setShowErrorModal(false);
  }

  function handlePartialSubstitutionDecipher() {
    setShowSubstitutionModal(false)
  }

  async function handleFullSubstitutionDecipher() {
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
        <NavBar/>

        <div className='mb-4'>
          <h1 className="display-4">Decrypter Tool</h1>
          <p className="lead">Use this tool to decrypt any Caesar, Transposition or Substitution cipher. For more information, please see the Encryption Methods page.</p>
        </div>

        <div className="d-flex flex-row justify-content-between">

          <div className="jumbotron" style={{width: "41%"}}>
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

          <div style={{position: "relative", width: "13%"}}>
            <Image src="/arrow-right.svg" layout="fill" objectFit="contain" />
          </div>
          
          <div className="jumbotron" style={{width: "41%"}}>
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
              {unknownCipherType &&
                <p> The plaintext for the ciphertext that you entered was encrypted using a <b> {unknownCipherType} </b> cipher. </p>
              }       
            </form>
          </div>
        
        </div>

        <Modal 
          show={showErrorModal}
          backdrop="static"
          keyboard={false}
          size="lg"
          aria-labelledby="contained-modal-title-vcenter"
          centered
        >
          <Modal.Header>
            <Modal.Title>Error</Modal.Title>
            <CloseButton onClick={handleErrorModalClose}/>
          </Modal.Header>
          <Modal.Body>{errorMessage}</Modal.Body>
          <Modal.Footer>
            <Button variant="primary" onClick={handleErrorModalClose}>
              Close
            </Button>
          </Modal.Footer>
        </Modal>

        <Modal 
          show={showSubstitutionModal}
          backdrop="static"
          keyboard={false}
          size="lg"
          aria-labelledby="contained-modal-title-vcenter"
        >
          <Modal.Header>
            <Modal.Title>Substitution Decryption Options</Modal.Title>
            <CloseButton onClick={handlePartialSubstitutionDecipher}/>
          </Modal.Header>
          <Modal.Body>
            <p>Doing a partial substitution decipher, the decrypter tool initially found {<b>{totalAmountPossibilities}</b>} possible keys for your ciphertext. You can choose to either view the plaintext using the currently known letters from the partial decipher (with _'s in the place of the unknown letters), or do a full decipher to potentially decrypt the remaining letters. </p>
            <p><b>Approximate Response Times for Full Decipher:</b></p>
            <ul>
              <li> {"<"} 1000 possible keys: 1-3 seconds</li>
            </ul>
          </Modal.Body>
          <Modal.Footer>
          <Button variant="primary" onClick={handlePartialSubstitutionDecipher}>
            Partial Decipher
          </Button>
          <Button variant="success" onClick={handleFullSubstitutionDecipher}>
            Full Decipher
          </Button>
          </Modal.Footer>
        </Modal>
            
      </div>
    </div>
  )
}