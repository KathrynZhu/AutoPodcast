import { initializeApp } from 'firebase/app';

const firebaseConfig = {
  apiKey: "...",
  authDomain: "...",
  databaseURL: "...",
  projectId: "...",
  storageBucket: "....",
  messagingSenderId: "...",
  appId: "..."
};

const firebase = initializeApp(firebaseConfig);