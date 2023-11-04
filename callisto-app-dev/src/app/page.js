import Image from 'next/image'
import styles from './styles/page.module.css'
import Navbar from './components/Navbar'

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <div className={styles.navbarcontainer}>
          <Navbar />
        </div>
        <div className={styles.gptcontainer}>
          
        </div>
      </div>
    </main>
  )
}
