import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Cipher Cracker</title>
      </Head>
      <div>
        <h1>Cipher Cracker</h1>
          <form>
            <select name="Cipher Type" defaultValue="Caesar">
              <option value="Caesar">Caesar</option>
              <option value="Transposition">Transposition</option>
              <option value="Substitution">Substitution</option>
            </select>
            <br></br>
            <br></br>
            <textarea name="textValue" placeholder="Write here" rows="20" cols="50" />
            <br></br>
            <button type="submit">Submit</button>
          </form>
      </div>
    </div>
  )
}
