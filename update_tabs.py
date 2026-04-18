import sys

new_content = r'''                <div class="flex flex-wrap justify-center solution-cards-container" style="gap: 2rem;">
                    <!-- Card 1 -->
                    <div class="p-8 solution-card cursor-pointer hover:border-blue-500 flex flex-col" onclick="showDetail('logistics')" data-tab="logistics" style="width: 280px; min-height: 280px; background: #09131e; border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; transition: all 0.3s ease;">
                        <div class="mb-5" style="width: 44px; height: 44px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(0, 150, 255, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-truck-moving text-lg text-blue-glow"></i></div>
                        <h3 class="font-bold mb-3 text-white">Logistics Solutions</h3>
                        <p class="text-gray-400 text-sm opacity-80 leading-relaxed mb-4 flex-grow">Land, Sea and Air Freight with comprehensive Warehousing & distribution.</p>
                        <div class="mt-auto"><span class="explore-btn" style="color: #2563eb; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif;">EXPLORE <i class="fas fa-arrow-right ml-1"></i></span></div>
                    </div>
                    <!-- Card 2 -->
                    <div class="p-8 solution-card cursor-pointer hover:border-blue-500 flex flex-col" onclick="showDetail('procurement')" data-tab="procurement" style="width: 280px; min-height: 280px; background: #09131e; border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; transition: all 0.3s ease;">
                        <div class="mb-5" style="width: 44px; height: 44px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(0, 150, 255, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-globe text-lg text-blue-glow"></i></div>
                        <h3 class="font-bold mb-3 text-white">Procurement Solutions</h3>
                        <p class="text-gray-400 text-sm opacity-80 leading-relaxed mb-4 flex-grow">Strategic sourcing and supply chain management for global markets.</p>
                        <div class="mt-auto"><span class="explore-btn" style="color: #2563eb; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif;">EXPLORE <i class="fas fa-arrow-right ml-1"></i></span></div>
                    </div>
                    <!-- Card 3 -->
                    <div class="p-8 solution-card cursor-pointer hover:border-blue-500 flex flex-col" onclick="showDetail('furniture')" data-tab="furniture" style="width: 280px; min-height: 280px; background: #09131e; border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; transition: all 0.3s ease;">
                        <div class="mb-5" style="width: 44px; height: 44px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(0, 150, 255, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-couch text-lg text-blue-glow"></i></div>
                        <h3 class="font-bold mb-3 text-white">Furniture Solutions</h3>
                        <p class="text-gray-400 text-sm opacity-80 leading-relaxed mb-4 flex-grow">Premium commercial and residential furniture sourcing.</p>
                        <div class="mt-auto"><span class="explore-btn" style="color: #2563eb; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif;">EXPLORE <i class="fas fa-arrow-right ml-1"></i></span></div>
                    </div>
                    <!-- Card 4 -->
                    <div class="p-8 solution-card cursor-pointer hover:border-blue-500 flex flex-col" onclick="showDetail('lighting')" data-tab="lighting" style="width: 280px; min-height: 280px; background: #09131e; border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; transition: all 0.3s ease;">
                        <div class="mb-5" style="width: 44px; height: 44px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(0, 150, 255, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-lightbulb text-lg text-blue-glow"></i></div>
                        <h3 class="font-bold mb-3 text-white">Lighting & Interior</h3>
                        <p class="text-gray-400 text-sm opacity-80 leading-relaxed mb-4 flex-grow">Innovative lighting systems and interior design support.</p>
                        <div class="mt-auto"><span class="explore-btn" style="color: #2563eb; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif;">EXPLORE <i class="fas fa-arrow-right ml-1"></i></span></div>
                    </div>
                    <!-- Card 5 -->
                    <div class="p-8 solution-card cursor-pointer hover:border-blue-500 flex flex-col" onclick="showDetail('it')" data-tab="it" style="width: 280px; min-height: 280px; background: #09131e; border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; transition: all 0.3s ease;">
                        <div class="mb-5" style="width: 44px; height: 44px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(0, 150, 255, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-laptop-code text-lg text-blue-glow"></i></div>
                        <h3 class="font-bold mb-3 text-white">IT Solutions</h3>
                        <p class="text-gray-400 text-sm opacity-80 leading-relaxed mb-4 flex-grow">Custom website development, app development and software solutions.</p>
                        <div class="mt-auto"><span class="explore-btn" style="color: #2563eb; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif;">EXPLORE <i class="fas fa-arrow-right ml-1"></i></span></div>
                    </div>
                    <!-- Card 6 -->
                    <div class="p-8 solution-card cursor-pointer hover:border-blue-500 flex flex-col" onclick="showDetail('hospitality')" data-tab="hospitality" style="width: 280px; min-height: 280px; background: #09131e; border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; transition: all 0.3s ease;">
                        <div class="mb-5" style="width: 44px; height: 44px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(0, 150, 255, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-hotel text-lg text-blue-glow"></i></div>
                        <h3 class="font-bold mb-3 text-white">Hospitality Supplies</h3>
                        <p class="text-gray-400 text-sm opacity-80 leading-relaxed mb-4 flex-grow">Comprehensive FF&E and OS&E solutions for hotels.</p>
                        <div class="mt-auto"><span class="explore-btn" style="color: #2563eb; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif;">EXPLORE <i class="fas fa-arrow-right ml-1"></i></span></div>
                    </div>
                    <!-- Card 7 -->
                    <div class="p-8 solution-card cursor-pointer hover:border-blue-500 flex flex-col" onclick="showDetail('building')" data-tab="building" style="width: 280px; min-height: 280px; background: #09131e; border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; transition: all 0.3s ease;">
                        <div class="mb-5" style="width: 44px; height: 44px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(0, 150, 255, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-building text-lg text-blue-glow"></i></div>
                        <h3 class="font-bold mb-3 text-white">Building Materials</h3>
                        <p class="text-gray-400 text-sm opacity-80 leading-relaxed mb-4 flex-grow">Premium quality sourcing for structural and finishing materials.</p>
                        <div class="mt-auto"><span class="explore-btn" style="color: #2563eb; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif;">EXPLORE <i class="fas fa-arrow-right ml-1"></i></span></div>
                    </div>
                    <!-- Card 8 -->
                    <div class="p-8 solution-card cursor-pointer hover:border-blue-500 flex flex-col" onclick="showDetail('industrial')" data-tab="industrial" style="width: 280px; min-height: 280px; background: #09131e; border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; transition: all 0.3s ease;">
                        <div class="mb-5" style="width: 44px; height: 44px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(0, 150, 255, 0.3); border-radius: 10px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-industry text-lg text-blue-glow"></i></div>
                        <h3 class="font-bold mb-3 text-white">Industrial Solutions</h3>
                        <p class="text-gray-400 text-sm opacity-80 leading-relaxed mb-4 flex-grow">Procurement of machinery, equipment and industrial parts.</p>
                        <div class="mt-auto"><span class="explore-btn" style="color: #2563eb; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif;">EXPLORE <i class="fas fa-arrow-right ml-1"></i></span></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 4: Dynamic Details Section -->
        <section id="dynamic-detail" class="py-32 relative overflow-hidden bg-black transition-opacity duration-500" style="display: none; opacity: 0;">
            <div class="container mx-auto px-6 relative z-10">
                <div class="innov-layout">
                    <div class="innov-text">
                        <span class="section-tag" id="dyn-tag">MATERIALS</span>
                        <h2 class="text-4xl md:text-5xl font-bold mt-6 mb-8" id="dyn-title">Building Materials & <span class="gradient-text">Finishing Solutions</span></h2>
                        <p class="text-gray-400 mb-10 leading-relaxed text-lg" id="dyn-desc">We specialize in sourcing high-quality finishing and interior materials tailored for residential, commercial and hospitality projects — connecting you to the world\'s best suppliers.</p>
                        <div class="innov-stats" id="dyn-stats">
                            <div class="innov-stat"><h3>500+</h3><p>Projects</p></div>
                            <div class="innov-stat"><h3>50+</h3><p>Suppliers</p></div>
                            <div class="innov-stat"><h3>100%</h3><p>Quality Rate</p></div>
                        </div>
                    </div>
                    <div class="mat-cards" id="dyn-cards">
                        <!-- Populated dynamically -->
                    </div>
                </div>
            </div>
        </section>

        <!-- Script for Dynamic Tabs -->
        <script>
            const solutionsData = {
                logistics: {
                    tag: 'LOGISTICS',
                    title: 'Global <span class="gradient-text">Logistics</span>',
                    desc: 'Land, Sea and Air Freight with comprehensive Warehousing & distribution. We ensure your cargo reaches its destination exactly on time through optimized channels.',
                    stats: [{val: '10K+', label: 'Shipments'}, {val: '50+', label: 'Countries'}, {val: '99%', label: 'On-Time'}],
                    cards: [
                        {icon: 'fa-truck', title: 'Land Freight', desc: 'Secure and reliable ground transport spanning key regional hubs.'},
                        {icon: 'fa-ship', title: 'Sea Freight', desc: 'Cost-effective global ocean shipping and port-to-door fulfillment.'},
                        {icon: 'fa-plane', title: 'Air Freight', desc: 'Expedited aerial delivery solutions for time-critical project timelines.'}
                    ]
                },
                procurement: {
                    tag: 'PROCUREMENT',
                    title: 'Strategic <span class="gradient-text">Procurement</span>',
                    desc: 'A robust and scalable sourcing system designed to streamline your entire supply chain and unlock maximum financial value in global markets.',
                    stats: [{val: '500+', label: 'Suppliers'}, {val: '30+', label: 'Categories'}, {val: '100%', label: 'Vetted'}],
                    cards: [
                        {icon: 'fa-search-dollar', title: 'Sourcing Optimization', desc: 'Intelligently seeking the highest quality products at unmatched direct-to-market prices.'},
                        {icon: 'fa-file-contract', title: 'Contract Management', desc: 'Ensuring bulletproof legal and trade agreements with certified global manufacturers.'},
                        {icon: 'fa-handshake', title: 'Vendor Relations', desc: 'Building seamless and sustained long-term relationships with critical suppliers.'}
                    ]
                },
                furniture: {
                    tag: 'FURNITURE',
                    title: 'Premium <span class="gradient-text">Furniture Solutions</span>',
                    desc: 'Unparalleled commercial and residential furniture sourcing. We curate and deliver world-class aesthetic solutions for elite properties.',
                    stats: [{val: '1000+', label: 'Designs'}, {val: '20+', label: 'Brands'}, {val: '100%', label: 'Quality Assured'}],
                    cards: [
                        {icon: 'fa-couch', title: 'Commercial Layouts', desc: 'Durable, high-comfort installations for corporate offices and grand hospitality lobbies.'},
                        {icon: 'fa-chair', title: 'Residential Elegance', desc: 'Curated home, multi-family apartment and villa luxury setups.'},
                        {icon: 'fa-bed', title: 'Bespoke Pieces', desc: 'Custom-manufactured aesthetics designed strictly to architectural blueprints.'}
                    ]
                },
                lighting: {
                    tag: 'LIGHTING',
                    title: 'Innovative <span class="gradient-text">Lighting</span>',
                    desc: 'State-of-the-art lighting technologies coupled with brilliant interior design support to dramatically elevate your commercial and residential environments.',
                    stats: [{val: '500+', label: 'Fixtures'}, {val: '15+', label: 'Brands'}, {val: '100%', label: 'Energy Efficient'}],
                    cards: [
                        {icon: 'fa-lightbulb', title: 'LED Systems', desc: 'Next-generation smart and energy-saving lighting integrations.'},
                        {icon: 'fa-gem', title: 'Decorative Fixtures', desc: 'Statement chandeliers, sconces and ambient luminaires.'},
                        {icon: 'fa-sun', title: 'Landscape & Facade', desc: 'Durable outdoor illumination for exterior architecture and gardens.'}
                    ]
                },
                it: {
                    tag: 'DIGITAL SOLUTIONS',
                    title: 'Custom <span class="gradient-text">Software & Web</span>',
                    desc: 'We provide comprehensive digital solutions including custom website development, mobile apps and enterprise software systems designed to scale with your business.',
                    stats: [{val: '100+', label: 'Projects'}, {val: '20+', label: 'Technologies'}, {val: '24/7', label: 'Support'}],
                    cards: [
                        {icon: 'fa-code', title: 'Website Development', desc: 'High-performance, responsive websites built with the latest technologies.'},
                        {icon: 'fa-mobile-alt', title: 'App Development', desc: 'Native and cross-platform mobile applications for iOS and Android.'},
                        {icon: 'fa-laptop-code', title: 'Software Solutions', desc: 'Custom enterprise software and cloud-based systems for modern businesses.'}
                    ]
                },
                hospitality: {
                    tag: 'HOSPITALITY',
                    title: 'Comprehensive <span class="gradient-text">Hospitality</span>',
                    desc: 'Turnkey operational and aesthetic deployments for global hotels. We meticulously outfit entire properties to five-star standards.',
                    stats: [{val: '50+', label: 'Hotels'}, {val: '10K+', label: 'Rooms Outfitted'}, {val: '100%', label: 'Turnkey Ready'}],
                    cards: [
                        {icon: 'fa-hotel', title: 'FF&E Procurement', desc: 'Flawless procurement of Furniture, Fixtures and operational Equipment.'},
                        {icon: 'fa-utensils', title: 'OS&E Optimization', desc: 'Luxurious operating supplies, linens and daily amenities.'},
                        {icon: 'fa-glass-cheers', title: 'F&B Equipment', desc: 'Complete commercial kitchen apparatus and elegant dining setups.'}
                    ]
                },
                building: {
                    tag: 'MATERIALS',
                    title: 'Building Materials & <span class="gradient-text">Finishing Solutions</span>',
                    desc: 'We specialize in sourcing high-quality finishing and interior materials tailored for residential, commercial and hospitality projects — connecting you to the world\'s best suppliers.',
                    stats: [{val: '500+', label: 'Projects'}, {val: '50+', label: 'Suppliers'}, {val: '100%', label: 'Quality Rate'}],
                    cards: [
                        {icon: 'fa-layer-group', title: 'Tiles & Vinyl Flooring', desc: 'Premium tiles, marble, granite and vinyl flooring solutions.'},
                        {icon: 'fa-border-all', title: 'Interiors', desc: 'Wall cladding, panels and partition systems.'},
                        {icon: 'fa-faucet', title: 'Sanitary Ware', desc: 'Premium bathroom and sanitary fittings.'},
                        {icon: 'fa-lightbulb', title: 'Electrical & Lighting', desc: 'Fixtures, lighting accessories and hardware.'}
                    ]
                },
                industrial: {
                    tag: 'INDUSTRIAL',
                    title: 'Heavy <span class="gradient-text">Industrial Solutions</span>',
                    desc: 'Expert procurement of advanced machinery, precision equipment and industrial components serving robust processing architectures.',
                    stats: [{val: '100+', label: 'Machines'}, {val: '20+', label: 'Categories'}, {val: '100%', label: 'Certified Specs'}],
                    cards: [
                        {icon: 'fa-cogs', title: 'Industrial Machinery', desc: 'High-yield manufacturing and raw construction systems.'},
                        {icon: 'fa-tools', title: 'Industrial Parts', desc: 'Critical supply line replacement components and operational spares.'},
                        {icon: 'fa-industry', title: 'Plant Equipment', desc: 'Logistics and scaling for industrial and plant integrations.'}
                    ]
                }
            };

            function showDetail(tabId) {
                const data = solutionsData[tabId];
                if (!data) return;

                // Update visual active state of cards
                document.querySelectorAll('.solution-card').forEach(el => {
                    el.style.borderColor = 'rgba(255,255,255,0.03)';
                    el.style.backgroundColor = '#09131e';
                    el.style.transform = 'translateY(0)';
                });
                
                const activeCard = document.querySelector(".solution-card[data-tab='" + tabId + "']");
                if (activeCard) {
                    activeCard.style.borderColor = '#2563eb';
                    activeCard.style.backgroundColor = '#0c1a2c';
                    activeCard.style.transform = 'translateY(-5px)';
                }

                const detailSection = document.getElementById('dynamic-detail');
                
                // If it is hidden, display it but with 0 opacity
                if (detailSection.style.display === 'none') {
                    detailSection.style.display = 'block';
                }

                detailSection.style.opacity = '0';
                
                setTimeout(() => {
                    document.getElementById('dyn-tag').innerHTML = data.tag;
                    document.getElementById('dyn-title').innerHTML = data.title;
                    document.getElementById('dyn-desc').innerHTML = data.desc;

                    // Update stats
                    const statsHtml = data.stats.map(s => "<div class='innov-stat'><h3>" + s.val + "</h3><p>" + s.label + "</p></div>").join('');
                    document.getElementById('dyn-stats').innerHTML = statsHtml;

                    // Update cards
                    const cardsHtml = data.cards.map(c => "<div class='mat-card'><div class='mat-card-icon'><i class='fas " + c.icon + "'></i></div><div><h4 class='font-bold text-white mb-2'>" + c.title + "</h4><p class='text-gray-500 text-sm'>" + c.desc + "</p></div></div>").join('');
                    document.getElementById('dyn-cards').innerHTML = cardsHtml;
                    
                    detailSection.style.opacity = '1';
                    detailSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 200);
            }
        </script>
'''

with open('services.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
skip = False
for i, line in enumerate(lines):
    if line.strip() == '<div class="flex flex-wrap justify-center solution-cards-container" style="gap: 2rem;">':
        skip = True
        out.append(new_content + '\n')
    elif skip and line.strip() == '<!-- Section 5: Process -->':
        skip = False
    
    if not skip:
        out.append(line)

with open('services.html', 'w', encoding='utf-8') as f:
    f.writelines(out)

print("File successfully rewritten.")
