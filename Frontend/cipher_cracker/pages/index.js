import Head from 'next/head';
import Image from 'next/image';
import styles from '../styles/Home.module.css';
import apiurl from "../utils/apiurl";
import { useState } from "react";
import NavBar from "../components/NavBar.js"
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import CloseButton from 'react-bootstrap/CloseButton';
import Spinner from 'react-bootstrap/Spinner'

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

export default function Home() {

  const [cipherText, setCipherText] = useState("");
  const [cipherType, setCipherType] = useState("");
  const [plainText, setPlainText] = useState("");
  const [key, setKey] = useState("");

  const [showErrorModal, setShowErrorModal] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  
  const [showSubstitutionModal, setShowSubstitutionModal] = useState(false);
  const [totalAmountPossibilities, setTotalAmountPossibilities] = useState("");
  const [intersectedMapping, setIntersectedMapping] = useState({});
  const [buttonDisabled, setbuttonDisabled] = useState(false);

  const [decryptLoading, setDecryptLoading] = useState(false);
  const [fullDecipherLoading, setFullDecipherLoading] = useState(false);


  async function handleSubmit(event) {
    event.preventDefault();

    if (event.target.cipherText.value === "") {
      setErrorMessage("Ciphertext field cannot be left blank.");
      setShowErrorModal(true);
      return;
    }

    setDecryptLoading(true);
    
    setCipherText(event.target.cipherText.value);
    setCipherType(event.target.cipherType.value);
    const cipherTypeLocal = event.target.cipherType.value; // useState is asynchronous
    const apiurlFull = apiurl + cipherTypeLocal;

    if (cipherTypeLocal === "substitution") {
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
    setTotalAmountPossibilities("")
    setIntersectedMapping({})
    setbuttonDisabled(false)
    
    if (cipherTypeLocal === "unknown") {
      setCipherType(result.cipherType);
      setPlainText(result.result.plainText);

      if (result.cipherType === "substitution") {
        setShowSubstitutionModal(true)
        
        let amountPossible = result.result.totalAmountPossibilities;
        if (amountPossible != 1) {
          setTotalAmountPossibilities(amountPossible);
          if (amountPossible > 500000) {
            setbuttonDisabled(true);
          }
        } else {
          setTotalAmountPossibilities("infinite")
          setbuttonDisabled(true)
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
        
        if (cipherTypeLocal === "substitution") {
          setShowSubstitutionModal(true)

          let amountPossible = result.totalAmountPossibilities;
          if (amountPossible != 1) {
            setTotalAmountPossibilities(amountPossible);
            if (amountPossible > 500000) {
              setbuttonDisabled(true);
            }
          } else {
            setTotalAmountPossibilities("infinite")
            setbuttonDisabled(true)
          }
        
          setIntersectedMapping(result.intersectedMapping)
          const keyAsString = JSON.stringify(result.key)
          setKey(keyAsString)
        } else {
          setKey(result.key);
        }
      }
    }

    setDecryptLoading(false)
  }

  function estimateResponseTime() {
    if (totalAmountPossibilities === "infinite") {
      return "There are too many possible keys for full decipher"
    } else {
      const asNum = parseInt(totalAmountPossibilities);
  
      if (asNum < 100000) {
        return "1-3 seconds";
      } else if (asNum <= 200000) {
        return "Less than 1 minute";
      } else if (asNum <= 500000) {
        return "Less than 3 minutes"
      } else {
        return "There are too many possible keys for a full decipher. Try entering a longer ciphertext."
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
    setFullDecipherLoading(true);
    
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
    setFullDecipherLoading(false);
    setShowSubstitutionModal(false);
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
              <button type="submit" className="btn btn-primary btn-lg">
                Decrypt{" "}
                {decryptLoading && <span className="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>}
              </button>
            </form>
          </div>

          <div style={{position: "relative", width: "13%"}}>
            <Image src="/arrow-right.svg"  alt="Arrow Right" layout="fill" objectFit="contain" />
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
              <p className="lead">Encryption Method: {cipherType && 
                <b>{capitalizeFirstLetter(cipherType)} Cipher</b>}
              </p>
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

        {!decryptLoading &&
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
              <p>Doing a partial substitution decipher, the decrypter tool initially found {<b>{totalAmountPossibilities}</b>} possible keys for your ciphertext. You can choose to either view the plaintext using the currently known letters from the partial decipher (with _&apos;s in the place of the unknown letters), or do a full decipher to potentially decrypt the remaining letters. </p>
              <p>Your estimated response time for Full Decipher: <b>{estimateResponseTime(totalAmountPossibilities)}</b></p>
              <div className="accordion">
                <div className="accordion-item">
                  <h2 className="accordion-header">
                    <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="false" aria-controls="panelsStayOpen-collapseOne">
                      Approximate Response Times for Full Decipher:
                    </button>
                  </h2>
                  <div id="panelsStayOpen-collapseOne" className="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingOne">
                    <div className="accordion-body">
                    <ul>
                      <li> Less than 10 000 possible keys: ≈ 1-3 seconds</li>
                      <li> 10 000 - 200 000 possible keys: ≈ Less than 1 minute</li>
                      <li> 200 000 - 500 000 possible keys: ≈ Less than 3 minutes</li>
                      <li> More than 500 000 possible keys: Too many possible keys for a full decipher</li>
                    </ul>
                    </div>
                  </div>
                </div>
              </div>

            </Modal.Body>
            <Modal.Footer>
            <Button variant="primary" onClick={handlePartialSubstitutionDecipher}>
              Partial Decipher
            </Button>
            <Button variant="success" onClick={handleFullSubstitutionDecipher} disabled={buttonDisabled} >
              Full Decipher{" "}
              {fullDecipherLoading && <span className="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>}
            </Button>
            </Modal.Footer>
          </Modal>
        }
            
      </div>
    </div>
  )
}