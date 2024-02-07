import { useQuery } from '@tanstack/react-query';

const fetchJson = async (url) => {
  const response = await fetch(url);
  if (!response.ok) throw response;
  return response.json();
};



const fetchJsons = async (obj) => {
    // fetch
    const urls = Object.values(obj);
    const jsons = await Promise.all(urls.map(url => fetchJson(url)));
  
    // collect into obj
    const keys = Object.keys(obj);
    return Object.fromEntries(keys.map((key, i) => [key, jsons[i]]));
  }
  export const useJsonQuery = (url) => {
    //const entries = Object.entries(obj);
    const { data, isLoading, error } = useQuery({
      queryKey: [url],
      queryFn: () => fetchJson(url)
    });
  
    return [ data, isLoading, error ];
  };
  
 /* export const useJsonQueries = (obj) => {
    const entries = Object.entries(obj);
    const { data, isLoading, error } = useQuery({
      queryKey: entries,
      queryFn: () => fetchJsons(obj))
    });
    return [ data, isLoading, error ];
  };*/