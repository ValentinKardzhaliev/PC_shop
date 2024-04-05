import React, { useState, useContext } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart, faCartShopping, faUser, faSignOut, faBars, faGlobe } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';
import SearchForm from '../SearchForm/SearchForm'
import AuthContext from '../../contexts/AuthContext';
import './Header.css';

function Header() {
    const { user } = useContext(AuthContext);
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const [isPeripheryMenuOpen, setIsPeripheryMenuOpen] = useState(false);

    const toggleMenu = () => {
        setIsMenuOpen(prev => !prev);
        setIsPeripheryMenuOpen(false);
    };

    const togglePeripheryMenu = () => {
        setIsPeripheryMenuOpen(prev => !prev);
    };


    return (
        <header className="sticky-top">
            <nav className="navbar">
                <div className="navbar-element-container">
                    <div className="home">
                        <Link to="/">ByteBazaar</Link>
                    </div>
                    <div className="category-menu">
                        <div onClick={toggleMenu} className="category-menu-dropdown">
                            <FontAwesomeIcon icon={faBars} />
                            <div className="category-menu-text">
                                Menu
                            </div>
                        </div>
                        {isMenuOpen && (
                            <div className="category-menu-content">
                                {/* Your dropdown menu content here */}
                                <Link to="/catalog/computers" onClick={toggleMenu}>Computers</Link>
                                <Link to="/catalog/monitors" onClick={toggleMenu}>Monitors</Link>
                                <Link to="#" onClick={togglePeripheryMenu}>Periphery</Link>
                                <Link to="#">Accessories</Link>
                                {/*<Link to="/catalog/others">Others</Link>*/}
                            </div>
                        )}
                        {isPeripheryMenuOpen && (
                            <div className="category-periphery-menu-content">
                                <Link to="/catalog/keyboards" onClick={toggleMenu}>Keyboards</Link>
                                <Link to="/catalog/mice" onClick={toggleMenu}>Mice</Link>

                            </div>
                        )}
                    </div>
                    <div className="search-bar-section">
                        <SearchForm />
                    </div>
                    <div className="navbar-right-side">
                        {user.token ? (
                            <>
                                <Link to="/logout">
                                    <FontAwesomeIcon icon={faSignOut} />
                                </Link>
                                <Link to="/cart">
                                    <FontAwesomeIcon icon={faCartShopping} />
                                </Link>


                                <Link to="/likes">
                                    <FontAwesomeIcon icon={faHeart} />
                                </Link>

                                <Link to={'#'}><FontAwesomeIcon icon={faGlobe} /></Link>

                            </>
                        ) : (
                            <>
                                <Link to="/login">
                                    <FontAwesomeIcon icon={faUser} />
                                </Link>


                                <Link to="/cart">
                                    <FontAwesomeIcon icon={faCartShopping} />
                                </Link>


                                <Link to="/likes">
                                    <FontAwesomeIcon icon={faHeart} />
                                </Link>
                                <Link to={'#'}><FontAwesomeIcon icon={faGlobe} /></Link>

                            </>
                        )}

                    </div>
                </div>
            </nav>
        </header >
    );
}

export default Header;
