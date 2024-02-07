// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDHxRuctyP5EaCFPh3oMTJK1LcQkAu_oes",
  authDomain: "podcast-20bf8.firebaseapp.com",
  databaseURL: "https://podcast-20bf8-default-rtdb.firebaseio.com",
  projectId: "podcast-20bf8",
  storageBucket: "podcast-20bf8.appspot.com",
  messagingSenderId: "438252918256",
  appId: "1:438252918256:web:ca044dd99239ae25817935",
  measurementId: "G-00E5DR4HY0"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);