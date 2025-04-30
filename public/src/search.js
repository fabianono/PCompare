import React, { useState } from 'react'

function Search() {
    const [query, setQuery] = useState('');
    const [sort, setSort] = useState('');
    const [sort_dir, setSort_dir] = useState('');
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [currentItemIndex, setCurrentItemIndex] = useState(0);
    
    const handleSearch = async () => {
        setLoading(true);
        setResults(null); // Clear previous results
        try {
          const response = await fetch(`http://127.0.0.1:8000/zalora/data?query=${query}&sort=${sort}&sort_dir=${sort_dir}`);
          const data = await response.json();
          setResults(data); // Set results after fetching
        } catch (error) {
          console.error('Search failed:', error);
        } finally {
          setLoading(false);
        }
      };


    // Function to update the current image index for a product
    const updateImageIndex = (itemIndex, direction) => {
        setResults((prevResults) => ({
            ...prevResults, // Preserve the rest of the object
            items: prevResults.items.map((item, index) => {
                if (index === itemIndex) {
                    const totalImages = item.ImageList.length;
                    let newIndex = item.currentImageIndex || 0;
                    
                    if (direction === 'next') {
                        // Increment index, but make sure it doesn't exceed totalImages - 1
                        newIndex = Math.min(newIndex + 1, totalImages - 1);
                    } else if (direction === 'prev') {
                        // Decrement index, but make sure it doesn't go below 0
                        newIndex = Math.max(newIndex - 1, 0);
                    }
                    return { ...item, currentImageIndex: newIndex };
                }
    
                return item;
            })
        }));
    };

    return (
        <div>
            <input
                type="search"
                placeholder="Search product"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <button onClick={handleSearch}>Click to search</button>

            {/* Loading state */}
            {loading && <p>Loading...</p>}

            {/* Display results after data is fetched */}
            {results && results.items && results.items.length > 0 && (
                <div>
                    <ul className="carousel">
                        {/* Loop through each product */}
                        {results.items.map((item, itemIndex) => (
                            <li key={itemIndex} class = "productdetails">
                                
                                {/* Check if the item has ImageList */}
                                {item.ImageList && item.ImageList.length > 0 ? (
                                    <div>
                                        {/* Display a carousel for each item */}
                                        <div className="image-carousel">
                                            <img
                                                src={item.ImageList[item.currentImageIndex || 0]} // Default to first image if no index is set
                                                alt={item.Name}
                                                style={{ width: '300px', height: 'auto' }}
                                            />
                                            <div className="carousel-controls">
                                                <button onClick={() => updateImageIndex(itemIndex, 'prev')}>
                                                    Prev
                                                </button>
                                                <button onClick={() => updateImageIndex(itemIndex, 'next')}>
                                                    Next
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                ) : (
                                    <p>No images available for this product</p>
                                )}
                                

                                <label className="itemname">{item.Name}</label>
                                <span className="price">{item.Price}</span>
                                <span className="brand">{item.Brand}</span>
                                <span className="seller">{results.seller}</span>
                                <span className="avg_rating">{item.ReviewStatistics.AvgRating}</span>

                                <a class="productlink" href = {item.ProductUrl} target = "_blank">Go to site</a>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default Search;
