// Import GSAP and Three.js are already in HTML via CDN for simplicity in this environment
// but we'll use them here.

document.addEventListener('DOMContentLoaded', () => {
    initAnimations();
    initGlobe();
    initHeroBackground();
    initHeaderScroll();
    initTradeLines();
});

function initTradeLines() {
    const container = document.getElementById('trade-lines-bg');
    if (!container) return;
    const canvas = document.createElement('canvas');
    container.appendChild(canvas);
    const ctx = canvas.getContext('2d');
    let w, h;
    const lines = [];
    function resize() {
        w = canvas.width = container.clientWidth;
        h = canvas.height = container.clientHeight;
    }
    resize();
    window.addEventListener('resize', resize);
    class Line {
        constructor() {
            this.reset();
        }
        reset() {
            this.x = Math.random() * w;
            this.y = Math.random() * h;
            this.targetX = Math.random() * w;
            this.targetY = Math.random() * h;
            this.progress = 0;
            this.speed = 0.002 + Math.random() * 0.005;
        }
        update() {
            this.progress += this.speed;
            if (this.progress >= 1) this.reset();
        }
        draw() {
            ctx.strokeStyle = `rgba(0, 229, 255, ${Math.sin(this.progress * Math.PI) * 0.3})`;
            ctx.beginPath();
            ctx.moveTo(this.x, this.y);
            ctx.lineTo(this.x + (this.targetX - this.x) * this.progress, this.y + (this.targetY - this.y) * this.progress);
            ctx.stroke();
        }
    }
    for (let i = 0; i < 20; i++) lines.push(new Line());
    function animate() {
        ctx.clearRect(0, 0, w, h);
        lines.forEach(l => { l.update(); l.draw(); });
        requestAnimationFrame(animate);
    }
    animate();
}

function initAnimations() {
    gsap.registerPlugin(ScrollTrigger);

    // Hero Animations
    const heroTl = gsap.timeline();
    heroTl.to('h1', { opacity: 1, y: 0, duration: 1, ease: 'power4.out' })
        .to('h2', { opacity: 1, y: 0, duration: 0.8, ease: 'power4.out' }, '-=0.6')
        .to('p', { opacity: 1, y: 0, duration: 0.8, ease: 'power4.out' }, '-=0.6')
        .to('.hero-content .flex', { opacity: 1, y: 0, duration: 0.8, ease: 'power4.out' }, '-=0.6');

    // Scroll Reveal Animations
    gsap.utils.toArray('.scroll-reveal').forEach((el) => {
        gsap.to(el, {
            scrollTrigger: {
                trigger: el,
                start: 'top 92%',
                toggleActions: 'play none none none'
            },
            opacity: 1,
            y: 0,
            duration: 0.7,
            ease: 'power2.out'
        });
    });

    // Masonry items reveal
    gsap.utils.toArray('.masonry-item').forEach((item, i) => {
        gsap.from(item, {
            scrollTrigger: {
                trigger: item,
                start: 'top 90%',
            },
            y: 50,
            opacity: 0,
            duration: 0.8,
            delay: i % 3 * 0.2
        });
    });

}

function initHeaderScroll() {
    const header = document.getElementById('header');
    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    const isHomePage = window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname === '/GLOBAL%20TRADERS/' || window.location.pathname.includes('index.html');

    if (!isHomePage) {
        header.classList.add('scrolled');
    }

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50 || !isHomePage) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('open');
            const icon = menuToggle.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-bars');
                icon.classList.toggle('fa-times');
            }
        });

        // Close menu when a link is clicked
        navLinks.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('open');
                const icon = menuToggle.querySelector('i');
                if (icon) {
                    icon.classList.add('fa-bars');
                    icon.classList.remove('fa-times');
                }
            });
        });
    }
}

// initTimeline removed — old timeline section replaced with Innovación layout

function initGlobe() {
    const container = document.getElementById('globe-container');
    if (!container) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);

    // Create Globe
    const geometry = new THREE.SphereGeometry(2.5, 64, 64);
    const material = new THREE.MeshPhongMaterial({
        color: 0x00e5ff,
        wireframe: true,
        transparent: true,
        opacity: 0.5,
        emissive: 0x005577,
        emissiveIntensity: 0.5
    });
    const globe = new THREE.Mesh(geometry, material);
    scene.add(globe);

    // Add glowing points for cities/nodes
    const pointsGeometry = new THREE.BufferGeometry();
    const pointsCount = 300;
    const positions = new Float32Array(pointsCount * 3);
    for (let i = 0; i < pointsCount; i++) {
        const phi = Math.acos(-1 + (2 * i) / pointsCount);
        const theta = Math.sqrt(pointsCount * Math.PI) * phi;
        positions[i * 3] = 2.55 * Math.cos(theta) * Math.sin(phi);
        positions[i * 3 + 1] = 2.55 * Math.sin(theta) * Math.sin(phi);
        positions[i * 3 + 2] = 2.55 * Math.cos(phi);
    }
    pointsGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    const pointsMaterial = new THREE.PointsMaterial({
        color: 0x00e5ff,
        size: 0.05,
        transparent: true,
        opacity: 0.8
    });
    const points = new THREE.Points(pointsGeometry, pointsMaterial);
    globe.add(points);

    // Trade routes (Arcs)
    const createArc = () => {
        const curve = new THREE.CubicBezierCurve3(
            new THREE.Vector3(2 * Math.random() - 1, 2 * Math.random() - 1, 2 * Math.random() - 1).normalize().multiplyScalar(2),
            new THREE.Vector3(3 * Math.random() - 1.5, 3 * Math.random() - 1.5, 3 * Math.random() - 1.5),
            new THREE.Vector3(3 * Math.random() - 1.5, 3 * Math.random() - 1.5, 3 * Math.random() - 1.5),
            new THREE.Vector3(2 * Math.random() - 1, 2 * Math.random() - 1, 2 * Math.random() - 1).normalize().multiplyScalar(2)
        );
        const points = curve.getPoints(50);
        const geometry = new THREE.BufferGeometry().setFromPoints(points);
        const material = new THREE.LineBasicMaterial({ color: 0x00e5ff, transparent: true, opacity: 0.2 });
        return new THREE.Line(geometry, material);
    };

    for (let i = 0; i < 30; i++) {
        globe.add(createArc());
    }

    const light = new THREE.PointLight(0xffffff, 2, 100);
    light.position.set(10, 10, 10);
    scene.add(light);
    scene.add(new THREE.AmbientLight(0xffffff, 0.5));

    camera.position.z = 6;

    function animate() {
        requestAnimationFrame(animate);
        globe.rotation.y += 0.005;
        globe.rotation.x += 0.002;
        renderer.render(scene, camera);
    }
    animate();

    window.addEventListener('resize', () => {
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });
}

function initHeroBackground() {
    const container = document.getElementById('hero-canvas-container');
    if (!container) return;

    const canvas = document.createElement('canvas');
    container.appendChild(canvas);
    const ctx = canvas.getContext('2d');

    let width, height;
    const particles = [];

    function resize() {
        width = canvas.width = container.clientWidth;
        height = canvas.height = container.clientHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = (Math.random() - 0.5) * 0.5;
            this.size = Math.random() * 2;
        }
        update() {
            this.x += this.vx;
            this.y += this.vy;
            if (this.x < 0 || this.x > width) this.vx *= -1;
            if (this.y < 0 || this.y > height) this.vy *= -1;
        }
        draw() {
            ctx.fillStyle = 'rgba(0, 229, 255, 0.2)';
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    for (let i = 0; i < 100; i++) particles.push(new Particle());

    function animate() {
        ctx.clearRect(0, 0, width, height);

        // Draw grid
        ctx.strokeStyle = 'rgba(0, 229, 255, 0.05)';
        ctx.lineWidth = 1;
        const spacing = 50;
        for (let x = 0; x < width; x += spacing) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
        }
        for (let y = 0; y < height; y += spacing) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
        }

        particles.forEach(p => {
            p.update();
            p.draw();
        });
        requestAnimationFrame(animate);
    }
    animate();
}

function initWorldMapZoom() {
    const svg = document.getElementById('world-map-svg');
    const section = document.getElementById('world-map-section');
    const tagline = document.querySelector('.world-map-tagline');
    const scrollHint = document.querySelector('.world-map-scroll-hint');

    if (!svg || !section) return;

    // Zoom toward Asia / Middle East — the heart of global trade routes
    // SVG viewBox is 2000×1000; target focal point ~(1150, 360)
    const targetXFrac = 1150 / 2000; // 0.575
    const targetYFrac = 360 / 1000;  // 0.360
    const maxScale = 4.5;

    // Set transform-origin to the focal point expressed as percentages
    svg.style.transformOrigin = `${targetXFrac * 100}% ${targetYFrac * 100}%`;

    gsap.registerPlugin(ScrollTrigger);

    // Main zoom tween — tied 1-to-1 with scroll position (scrub)
    const zoomTl = gsap.timeline({
        scrollTrigger: {
            trigger: section,
            start: 'top top',
            end: 'bottom bottom',
            scrub: 1.8,
            pin: false,
        }
    });

    zoomTl.to(svg, {
        scale: maxScale,
        ease: 'none',
        duration: 1
    });

    // Overlay text fades out in the first 25 % of scroll travel
    gsap.to([tagline, scrollHint], {
        scrollTrigger: {
            trigger: section,
            start: 'top top',
            end: '25% top',
            scrub: true,
        },
        opacity: 0,
        ease: 'none',
    });

    // Continent fills brighten as zoom deepens for extra depth
    gsap.to('#world-map-svg .continent path', {
        scrollTrigger: {
            trigger: section,
            start: 'top top',
            end: 'bottom bottom',
            scrub: 2,
        },
        attr: { fill: '#1a4a30' },
        ease: 'none',
    });

    // Trade-route opacity rises to highlight connections while zooming
    gsap.to('#world-map-svg .trade-routes path', {
        scrollTrigger: {
            trigger: section,
            start: '20% top',
            end: '70% top',
            scrub: 1.5,
        },
        attr: { stroke: 'rgba(0,229,255,0.55)' },
        ease: 'none',
    });
}
