/**
 * Ding That type tester. Enhances the markup printed by the [ding_tester] shortcode.
 * Needs window.dingThatGlyphs (assets/js/glyph-data.js).
 */
( function () {
	'use strict';

	var SAMPLES = {
		gui: 'qrrrrrrwrrrrrre\nf pvIO f ;:\'" f\narrrrrrsrrrrrrd\nf 1234 fK__++Lf\nzrrrrrrxrrrrrrc',
		shapes: '8 6 2 4  v x  k h  ; : \'  + - = /',
		objects: 'h o s f   c b t a 3   e d F C'
	};
	var ORDER = [ 'gui', 'shapes', 'objects' ];

	function init( root ) {
		var data = window.dingThatGlyphs;
		if ( ! data ) {
			return;
		}
		var tabs = root.querySelectorAll( '[data-dt-font]' );
		var text = root.querySelector( '.dt-tester-text' );
		var size = root.querySelector( '.dt-tester-size' );
		var sizeOut = root.querySelector( '.dt-tester-size-value' );
		var out = root.querySelector( '.dt-tester-output' );
		var grid = root.querySelector( '.dt-tester-grid' );
		var title = root.querySelector( '.dt-tester-family' );
		var count = root.querySelector( '.dt-tester-count' );
		var status = root.querySelector( '.dt-tester-status' );
		var texts = {};
		var current = root.getAttribute( 'data-font' ) || 'gui';
		var timer;

		ORDER.forEach( function ( k ) {
			texts[ k ] = SAMPLES[ k ];
		} );
		if ( ORDER.indexOf( current ) < 0 ) {
			current = 'gui';
		}

		function announce( message ) {
			status.textContent = '';
			window.clearTimeout( timer );
			timer = window.setTimeout( function () {
				status.textContent = message;
			}, 50 );
		}

		function draw() {
			out.textContent = text.value;
			out.style.fontSize = size.value + 'px';
			sizeOut.textContent = size.value + ' px';
		}

		function render() {
			var family = data[ current ];
			Array.prototype.forEach.call( tabs, function ( tab ) {
				var on = tab.getAttribute( 'data-dt-font' ) === current;
				tab.setAttribute( 'aria-selected', on ? 'true' : 'false' );
				tab.tabIndex = on ? 0 : -1;
			} );
			title.textContent = family.family;
			count.textContent = family.glyphs.length + ' glyphs · ' + ( family.mono ? 'monospaced' : 'proportional' );
			text.value = texts[ current ];
			out.className = 'dt-tester-output dt-g dt-g--' + current;
			grid.innerHTML = '';
			family.glyphs.forEach( function ( g ) {
				var key = g[ 0 ];
				var ch = key || String.fromCodePoint( g[ 1 ] );
				var cap = key ? ( key === ' ' ? 'space' : key ) : 'U+' + g[ 1 ].toString( 16 ).toUpperCase();
				var b = document.createElement( 'button' );
				b.type = 'button';
				b.className = 'dt-tester-cell';
				b.setAttribute( 'data-char', ch );
				b.setAttribute( 'aria-label', 'Add ' + g[ 2 ] + ( key ? ', key ' + cap : '' ) );
				var pic = document.createElement( 'span' );
				pic.className = 'dt-g dt-g--' + current;
				pic.setAttribute( 'aria-hidden', 'true' );
				pic.textContent = ch;
				var meta = document.createElement( 'span' );
				meta.setAttribute( 'aria-hidden', 'true' );
				var kbd = document.createElement( 'kbd' );
				kbd.textContent = cap;
				meta.appendChild( kbd );
				meta.appendChild( document.createTextNode( g[ 2 ] ) );
				b.appendChild( pic );
				b.appendChild( meta );
				grid.appendChild( b );
			} );
			draw();
		}

		root.querySelector( '.dt-tester-tabs' ).addEventListener( 'click', function ( e ) {
			var tab = e.target.closest( '[data-dt-font]' );
			if ( tab ) {
				current = tab.getAttribute( 'data-dt-font' );
				render();
			}
		} );
		root.querySelector( '.dt-tester-tabs' ).addEventListener( 'keydown', function ( e ) {
			var i = ORDER.indexOf( current );
			if ( e.key === 'ArrowRight' || e.key === 'ArrowLeft' ) {
				e.preventDefault();
				current = ORDER[ ( i + ( e.key === 'ArrowRight' ? 1 : 2 ) ) % 3 ];
				render();
				root.querySelector( '[data-dt-font="' + current + '"]' ).focus();
			}
		} );
		text.addEventListener( 'input', function () {
			texts[ current ] = text.value;
			draw();
		} );
		size.addEventListener( 'input', draw );
		grid.addEventListener( 'click', function ( e ) {
			var b = e.target.closest( '.dt-tester-cell' );
			if ( ! b ) {
				return;
			}
			var c = b.getAttribute( 'data-char' );
			texts[ current ] += c;
			text.value = texts[ current ];
			draw();
			var label = b.getAttribute( 'aria-label' ).replace( /^Add /, '' );
			if ( navigator.clipboard && window.isSecureContext ) {
				navigator.clipboard.writeText( c ).then( function () {
					announce( 'Added ' + label + ' to the tester and copied it.' );
				}, function () {
					announce( 'Added ' + label + ' to the tester.' );
				} );
			} else {
				announce( 'Added ' + label + ' to the tester.' );
			}
		} );
		root.querySelector( '.dt-tester-reset' ).addEventListener( 'click', function () {
			texts[ current ] = SAMPLES[ current ];
			render();
			announce( 'Sample text restored.' );
		} );

		root.classList.add( 'is-ready' );
		render();
	}

	function boot() {
		Array.prototype.forEach.call( document.querySelectorAll( '.dt-tester' ), init );
	}
	if ( document.readyState === 'loading' ) {
		document.addEventListener( 'DOMContentLoaded', boot );
	} else {
		boot();
	}
}() );
