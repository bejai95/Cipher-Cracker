import Image from 'next/image'
import Link from "next/link";
import logo from "../public/logo.png"

export default function NarBar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-2">
      <div className="container-fluid">
        <Link href="/">
          <a className="navbar-brand"> <Image src={logo} alt="Cipher Cracker Logo "width={100} height={71} /> </a>
        </Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link href="/">
                <a className="nav-link active" aria-current="page">Home</a>
              </Link>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Encryption Methods</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Explanation Video</a>
            </li>
          </ul>
        </div>
        <div className="lead text-light" >
          By Bejai Cobbing
        </div>
      </div>
    </nav>
  )
}

