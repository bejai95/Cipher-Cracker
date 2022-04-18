import "bootstrap/dist/css/bootstrap.css";
import "../styles/globals.css";
import Head from "next/head";

import { useEffect } from "react";

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    import("bootstrap/dist/js/bootstrap");
  }, []);
  
  return (
    <>
      <Head>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      
      <Component {...pageProps} />;
    </>
  ) 
}

export default MyApp;