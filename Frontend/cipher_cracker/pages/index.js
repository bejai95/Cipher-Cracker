import Head from 'next/head';
import Image from 'next/image';
import styles from '../styles/Home.module.css';
import apiurl from "../utils/apiurl";
import { useState } from "react";

function NewlineText(props) {
  const text = props.text;
  const newText = text.split('\n').map(str => <p>{str}</p>);
  return newText;
}

export default function Home() {
  const [plainText, setPlainText] = useState("");
  const [key, setKey] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    
    const apiurlFull = apiurl + event.target.CipherType.value

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
    setPlainText(result.plainText)
    setKey(result.key)
  }
  
  return (
    <div className={styles.container}>
      <Head>
        <title>Cipher Cracker</title>
      </Head>
      <div>
        <h1>Cipher Cracker</h1>
          <form onSubmit={handleSubmit}>
            <select name="CipherType" defaultValue="Caesar">
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

      </div>
    </div>
  )
}
