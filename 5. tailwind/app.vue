<template>

    <head>
        <link rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <header class="bg-[url('assets/images/landing.jpg')] bg-cover">
        <section class="container mx-auto px-5 flex justify-center py-3 items-center text-white lg:justify-between">
            <div class="flex items-center space-x-2">
                <img src="assets/images/logo.png" alt="" class="w-20 h-16">
                <div class="pe-4 border-r-2 border-slate-500 lg:hidden">
                    <i class="fa fa-bars"></i>
                </div>
            </div>
            <div class="border-r-2 border-slate-500 lg:hidden">
                <i class="fa fa-search px-3"></i>
            </div>
            <nav class="space-x-3 hidden lg:flex">
                <a href="">Latest Courses</a>
                <a href="">Blog</a>
                <a href="">Openings</a>
                <a href="">Consultation</a>
                <a href="">Discounts</a>
                <a href="">Certificates</a>
            </nav>
            <div class="flex space-x-1 items-center ml-2">
                <i class="fa fa-user"></i>
                <a href="" class="after:content-['_/'] sm:text-sm text-xs">Login</a>
                <a href="" class="sm:text-sm text-xs">Register</a>
            </div>
        </section>

        <section class="text-white text-center container mx-auto pt-10 px-5 flex justify-center items-center">
            <div>
                <h1 class="text-xl leading-10">
                    Self-study, Gain experience, Enter the job market with TopLearn
                </h1>
            </div>
        </section>

        <section class="flex pb-25 items-center text-center justify-center pt-10">
            <div class="relative w-4/5 ">
                <input type="text" placeholder="What you wanna learn?"
                    class="bg-white w-full h-12 rounded-3xl pl-12 pr-5 shadow-2xl ring-8 ring-slate-300/30 outline-none lg:w-2/5" />
                <svg xmlns="http://www.w3.org/2000/svg"
                    class="w-5 h-5 text-gray-500 absolute left-4 top-1/2 transform -translate-y-1/2" fill="none"
                    viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M21 21l-4.35-4.35M16.65 16.65A7 7 0 1110 3a7 7 0 016.65 13.65z" />
                </svg>
            </div>
        </section>

        <section class="hidden lg:flex justify-center items-center text-center pb-15 space-x-20">
            <article class="text-white">
                <img src="assets/images/stat-student.png" alt="" class="w-32 h-32">
                <div>111,111</div>
                <div>Students</div>
            </article>
            <article class="text-white">
                <img src="assets/images/stat-teacher.png" alt="" class="w-32 h-32">
                <div>111,111</div>
                <div>Students</div>
            </article>
            <article class="text-white">
                <img src="assets/images/stat-time.png" alt="" class="w-32 h-32">
                <div>111,111</div>
                <div>Students</div>
            </article>
        </section>
    </header>

    <main>
        <section class="hidden lg:block pb-6 pt-5 shadow-md">
            <div class="container mx-auto flex justify-between mb-3">
                <nav class="flex items-center space-x-5">
                    <a href="">Programming</a>
                    <a href="">Web</a>
                    <a href="">Developing</a>
                    <a href="">Android</a>
                    <a href="">Language Models</a>
                </nav>
                <div class="flex items-center">
                    <img src="assets/images/vip.png" alt="" class="w-10 h-10">
                    <a href="" class="text-sky-400 text-sm">VIP Users</a>
                </div>
            </div>
        </section>

        <section class="mt-5 my-5 container mx-auto flex justify-center">
            <UCarousel v-slot="{ item }" arrows :items="items" class="max-w-3xs sm:max-w-md md:max-w-xl lg:max-w-2xl">
                <img :src="item" class="rounded-lg h-70 w-full">
            </UCarousel>
        </section>

        <section>
            <header class="container mx-auto flex flex-col space-y-4 ps-0 lg:flex-row lg:space-y-0 lg:justify-between">
                <div>
                    <h3 class="font-medium txt-lg">Latest Courses</h3>
                </div>
                <div class="flex items-center space-x-2">
                    <h6 class="font-medium text-sm">See All Courses</h6>
                    <i class="fa fa-arrow-right text-sky-500"></i>
                </div>
            </header>

            <section class="container mx-auto">
                <header class="ps-5 sm:ps-0">
                    <h6 class="border-b-3 text-sm md:text-sm lg:text-md border-sky-500 w-30 pt-6 pb-2">Web Programming
                    </h6>
                </header>

                <div class="flex flex-wrap space-y-4 px-3 mt-10 space-x-2 justify-center">
                    <div class="sm:w-10/22 md:w-10/32 lg:w-10/42 xl:w-10/52">
                        <article class="border-1 border-slate-200 rounded-lg shadow-xl">
                            <img src="assets/images/course.jpg" alt="">
                            <div class="py-5 px-3 space-y-3 border-b-2 border-slate-200 pb-3">
                                <p>Learning to Build a Website via Tailwind</p>
                                <i class="fa fa-user text-slate-300 mr-1"></i>
                                <a href="" class="text-slate-500 text-sm">Instructor</a>
                            </div>
                            <footer class="flex justify-between py-3">
                                <div class="flex items-center mx-3 space-x-2 text-sky-500">
                                    <i class="fa fa-clock mr-1"></i>
                                    <p>10:01:10</p>
                                </div>
                                <div class="text-green-600 text-md pr-2">
                                    <h6>Free</h6>
                                </div>
                            </footer>
                        </article>
                    </div>
                    <div class="sm:w-10/22 md:w-10/32 lg:w-10/42 xl:w-10/52">
                        <article class="border-1 border-slate-200 rounded-lg shadow-xl">
                            <img src="assets/images/course.jpg" alt="">
                            <div class="py-5 px-3 space-y-3 border-b-2 border-slate-200 pb-3">
                                <p>Learning to Build a Website via Tailwind</p>
                                <i class="fa fa-user text-slate-300 mr-1"></i>
                                <a href="" class="text-slate-500 text-sm">Instructor</a>
                            </div>
                            <footer class="flex justify-between py-3">
                                <div class="flex items-center mx-3 space-x-2 text-sky-500">
                                    <i class="fa fa-clock mr-1"></i>
                                    <p>10:01:10</p>
                                </div>
                                <div class="text-green-600 text-md pr-2">
                                    <h6>Free</h6>
                                </div>
                            </footer>
                        </article>
                    </div>
                    <div class="sm:w-10/22 md:w-10/32 lg:w-10/42 xl:w-10/52">
                        <article class="border-1 border-slate-200 rounded-lg shadow-xl">
                            <img src="assets/images/course.jpg" alt="">
                            <div class="py-5 px-3 space-y-3 border-b-2 border-slate-200 pb-3">
                                <p>Learning to Build a Website via Tailwind</p>
                                <i class="fa fa-user text-slate-300 mr-1"></i>
                                <a href="" class="text-slate-500 text-sm">Instructor</a>
                            </div>
                            <footer class="flex justify-between py-3">
                                <div class="flex items-center mx-3 space-x-2 text-sky-500">
                                    <i class="fa fa-clock mr-1"></i>
                                    <p>10:01:10</p>
                                </div>
                                <div class="text-green-600 text-md pr-2">
                                    <h6>Free</h6>
                                </div>
                            </footer>
                        </article>
                    </div>
                    <div class="sm:w-10/22 md:w-10/32 lg:w-10/42 xl:w-10/52">
                        <article class="border-1 border-slate-200 rounded-lg shadow-xl">
                            <img src="assets/images/course.jpg" alt="">
                            <div class="py-5 px-3 space-y-3 border-b-2 border-slate-200 pb-3">
                                <p>Learning to Build a Website via Tailwind</p>
                                <i class="fa fa-user text-slate-300 mr-1"></i>
                                <a href="" class="text-slate-500 text-sm">Instructor</a>
                            </div>
                            <footer class="flex justify-between py-3">
                                <div class="flex items-center mx-3 space-x-2 text-sky-500">
                                    <i class="fa fa-clock mr-1"></i>
                                    <p>10:01:10</p>
                                </div>
                                <div class="text-green-600 text-md pr-2">
                                    <h6>Free</h6>
                                </div>
                            </footer>
                        </article>
                    </div>
                </div>
            </section>
        </section>

        <section class="mt-15 bg-slate-100 py-10">
            <header class="container mx-auto flex flex-col space-y-4 ps-0 lg:flex-row lg:space-y-0 lg:justify-between">
                <div>
                    <h3 class="font-medium txt-lg">Latest Blogs</h3>
                </div>
                <div class="flex items-center space-x-2">
                    <h6 class="font-medium text-sm">See All Blogs</h6>
                    <i class="fa fa-arrow-right text-sky-500"></i>
                </div>
            </header>

            <section class="container mx-auto bg-transparent">
                <div class="flex flex-wrap space-y-4 px-3 mt-10 space-x-2 justify-center">
                    <div class="sm:w-10/22 md:w-10/32 lg:w-10/42 xl:w-10/52">
                        <article class="border-1 border-slate-200 rounded-lg shadow-xl ">
                            <img src="assets/images/blog.jpg" alt="" class="rounded-lg">
                            <div class="p-5">
                                <h3 class="text-slate-900 mb-3 text-sm text-justify">Lorem ipsum dolor sit amet,
                                    consectetur.</h3>
                                <p class="text-sm leading-6 text-slate-600 text-justify">Lorem ipsum dolor sit amet,
                                    consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
                                    magna aliqua Egestas purus viverra accumsan in nisl.</p>
                            </div>
                            <footer class="p-5 border-t flex justify-between">
                                <section class="flex space-x-3">
                                    <div class="flex items-center space-x-2">
                                        <i class="fa fa-eye text-sm text-slate-300 mt-0.5"></i>
                                        <p>11</p>
                                    </div>
                                    <div class="flex items-center  space-x-2">
                                        <i class="fa fa-envelope text-sm text-slate-300 mt-0.5"></i>
                                        <p>11</p>
                                    </div>
                                </section>
                                <section>
                                    <div class="flex items-center space-x-2">
                                        <i class="fa fa-user text-sky-500 text-sm"></i>
                                        <p>Writer</p>
                                    </div>
                                </section>
                            </footer>
                        </article>
                    </div>
                    <div class="sm:w-10/22 md:w-10/32 lg:w-10/42 xl:w-10/52">
                        <article class="border-1 border-slate-200 rounded-lg shadow-xl ">
                            <img src="assets/images/blog.jpg" alt="" class="rounded-lg">
                            <div class="p-5">
                                <h3 class="text-slate-900 mb-3 text-sm text-justify">Lorem ipsum dolor sit amet,
                                    consectetur.</h3>
                                <p class="text-sm leading-6 text-slate-600 text-justify">Lorem ipsum dolor sit amet,
                                    consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
                                    magna aliqua Egestas purus viverra accumsan in nisl.</p>
                            </div>
                            <footer class="p-5 border-t flex justify-between">
                                <section class="flex space-x-3">
                                    <div class="flex items-center space-x-2">
                                        <i class="fa fa-eye text-sm text-slate-300 mt-0.5"></i>
                                        <p>11</p>
                                    </div>
                                    <div class="flex items-center  space-x-2">
                                        <i class="fa fa-envelope text-sm text-slate-300 mt-0.5"></i>
                                        <p>11</p>
                                    </div>
                                </section>
                                <section>
                                    <div class="flex items-center space-x-2">
                                        <i class="fa fa-user text-sky-500 text-sm"></i>
                                        <p>Writer</p>
                                    </div>
                                </section>
                            </footer>
                        </article>
                    </div>
                    <div class="sm:w-10/22 md:w-10/32 lg:w-10/42 xl:w-10/52">
                        <article class="border-1 border-slate-200 rounded-lg shadow-xl ">
                            <img src="assets/images/blog.jpg" alt="" class="rounded-lg">
                            <div class="p-5">
                                <h3 class="text-slate-900 mb-3 text-sm text-justify">Lorem ipsum dolor sit amet,
                                    consectetur.</h3>
                                <p class="text-sm leading-6 text-slate-600 text-justify">Lorem ipsum dolor sit amet,
                                    consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
                                    magna aliqua Egestas purus viverra accumsan in nisl.</p>
                            </div>
                            <footer class="p-5 border-t flex justify-between">
                                <section class="flex space-x-3">
                                    <div class="flex items-center space-x-2">
                                        <i class="fa fa-eye text-sm text-slate-300 mt-0.5"></i>
                                        <p>11</p>
                                    </div>
                                    <div class="flex items-center  space-x-2">
                                        <i class="fa fa-envelope text-sm text-slate-300 mt-0.5"></i>
                                        <p>11</p>
                                    </div>
                                </section>
                                <section>
                                    <div class="flex items-center space-x-2">
                                        <i class="fa fa-user text-sky-500 text-sm"></i>
                                        <p>Writer</p>
                                    </div>
                                </section>
                            </footer>
                        </article>
                    </div>
                    <div class="sm:w-10/22 md:w-10/32 lg:w-10/42 xl:w-10/52">
                        <article class="border-1 border-slate-200 rounded-lg shadow-xl ">
                            <img src="assets/images/blog.jpg" alt="" class="rounded-lg">
                            <div class="p-5">
                                <h3 class="text-slate-900 mb-3 text-sm text-justify">Lorem ipsum dolor sit amet,
                                    consectetur.</h3>
                                <p class="text-sm leading-6 text-slate-600 text-justify">Lorem ipsum dolor sit amet,
                                    consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
                                    magna aliqua Egestas purus viverra accumsan in nisl.</p>
                            </div>
                            <footer class="p-5 border-t flex justify-between">
                                <section class="flex space-x-3">
                                    <div class="flex items-center space-x-2">
                                        <i class="fa fa-eye text-sm text-slate-300 mt-0.5"></i>
                                        <p>11</p>
                                    </div>
                                    <div class="flex items-center  space-x-2">
                                        <i class="fa fa-envelope text-sm text-slate-300 mt-0.5"></i>
                                        <p>11</p>
                                    </div>
                                </section>
                                <section>
                                    <div class="flex items-center space-x-2">
                                        <i class="fa fa-user text-sky-500 text-sm"></i>
                                        <p>Writer</p>
                                    </div>
                                </section>
                            </footer>
                        </article>
                    </div>
                </div>
            </section>
        </section>
    </main>

    <footer>
        <div class="bg-blue-950 py-2">

            <section class="mb-15 mt-10">
                <div class="flex justify-center items-center">
                    <input type="text" class="bg-white rounded-lg p-1.5 h-3/5" placeholder="Newsletter">
                    <button class="bg-green-500 p-1.5 rounded-lg ml-0.5 h-3/5">Submit</button>
                </div>
            </section>

            <section class="">
                <div class="flex items-center justify-center space-x-2 mb-15">
                    <div class="bg-gray-400 w-15 h-15 rounded-2xl p-1">
                        <img src="assets/images/f-logo1.png" class="" alt="">
                    </div>
                    <div class="bg-gray-400 w-15 h-15 rounded-2xl p-1">
                        <img src="assets/images/f-logo2.png" class="" alt="">
                    </div>
                </div>
            </section>

            <section class="mb-15">
                <ul class="list-disc px-7 flex flex-wrap items-center space-x-15 justify-center text-white">
                    <li>Lorem ipsum dolor sit</li>
                    <li>amet, consectetur adipiscing</li>
                    <li>elit, sed do eiusmod tempor </li>
                    <li>incididunt ut labore et dolore</li>
                    <li>magna aliqua. Egestas</li>
                </ul>
            </section>

            <section>
                <div class="flex items-center justify-center space-x-2">
                    <div class="rounded-full text-center">
                        <i class="fa fa-telegram" style="color:white"></i>
                    </div>
                    <div>
                        <i class="fa fa-instagram" style="color:white"></i>
                    </div>
                </div>
            </section>
        </div>
        <div class="text-center py-1">
            <p>All Right Reserved</p>
        </div>
    </footer>
</template>
<script setup lang="ts">
const items = [
    'https://picsum.photos/640/640?random=1',
    'https://picsum.photos/640/640?random=2',
    'https://picsum.photos/640/640?random=3',
]
</script>