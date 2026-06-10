questions = [
    {
        "question": "When a client sends an HTTP/1.1 request to a server, which protocol at the Transport Layer is responsible for ensuring the message is broken into segments, delivered reliably, and reassembled in the correct order?",
        "options": [
            "A) Internet Protocol (IP)",
            "B) Transmission Control Protocol (TCP)",
            "C) User Datagram Protocol (UDP)",
            "D) HyperText Transfer Protocol (HTTP)"
        ],
        "answer": "B",
        "reason": "TCP is responsible for reliable delivery at the Transport Layer. It breaks data into segments, checks that they arrive, and reassembles them in the correct order."
    },
    {
        "question": "In the 2026 Modern-Web update, the HTTP/3 protocol introduced a major shift in transport architecture. Which underlying technology does HTTP/3 use to provide faster handshakes and better resilience to packet loss compared to its predecessors?",
        "options": [
            "A) Binary Framing over TCP",
            "B) Header Compression (HPACK)",
            "C) QUIC over UDP",
            "D) Layer 2 Tunneling Protocol"
        ],
        "answer": "C",
        "reason": "HTTP/3 uses QUIC, which runs over UDP. QUIC improves connection setup speed and handles packet loss better than older TCP-based HTTP versions."
    },
    {
        "question": "If a web developer wants to ensure that a browser only re-downloads an image if the content on the server has actually changed, which HTTP response header provides a unique hash or identifier for that specific version of the resource?",
        "options": [
            "A) Last-Modified",
            "B) Cache-Control",
            "C) ETag",
            "D) Expires"
        ],
        "answer": "C",
        "reason": "An ETag is a unique identifier for a specific version of a resource. The browser can compare it with the server's version to decide whether it needs to download the resource again."
    },
    {
        "question": "A Uniform Resource Locator (URL) consists of several parts. Which specific component is used by the browser to jump to a specific section within a document but is strictly not sent to the web server during the HTTP request?",
        "options": [
            "A) Query string",
            "B) Resource path",
            "C) Fragment identifier (#)",
            "D) Authority (Host)"
        ],
        "answer": "C",
        "reason": "The fragment identifier, written after the # symbol, is handled by the browser. It is used to jump to a section of the page and is not sent to the server."
    },
    {
        "question": "According to the HTTP standard, status codes are divided into classes. If a client receives a 307 Temporary Redirect code, what is the expected behavior of the user agent?",
        "options": [
            "A) Treat the resource as permanently moved and update all bookmarks.",
            "B) Display a Not Found error page to the user.",
            "C) Repeat the request to the new URI provided in the Location header.",
            "D) Prompt the user for a username and password to access the resource."
        ],
        "answer": "C",
        "reason": "A 307 Temporary Redirect tells the client to repeat the same request at the new URI given in the Location header. It is temporary, so bookmarks should not be permanently updated."
    },
    {
        "question": "Web servers must distinguish between different types of requests. What is the fundamental difference in how a server handles a request for a static file versus a request for a program such as a Java Servlet?",
        "options": [
            "A) Files are sent using ASCII while programs are sent using Binary.",
            "B) Files are handled by the IP layer while programs are handled by TCP.",
            "C) Files are sent as-is, while programs are executed to generate a dynamic body.",
            "D) Files require port 80 while programs require port 443."
        ],
        "answer": "C",
        "reason": "A static file is returned directly to the client. A program, such as a servlet, is executed on the server and produces dynamic content as the response body."
    },
    {
        "question": "In modern web architecture, Progressive Web Apps aim to provide a native-like experience. Which component runs in the background to intercept network requests and enable offline functionality?",
        "options": [
            "A) WebAssembly (Wasm)",
            "B) JSON Web Token (JWT)",
            "C) Service Worker",
            "D) Virtual DOM"
        ],
        "answer": "C",
        "reason": "A Service Worker runs in the background of a web app. It can intercept network requests, cache resources, and allow offline functionality."
    },
    {
        "question": "When configuring a Tomcat web server, the Coyote component is used to manage external communication. Which of the following is a typical task performed within this configuration?",
        "options": [
            "A) Setting the maximum number of simultaneous threads for connections.",
            "B) Mapping specific URIs to internal folder structures.",
            "C) Defining password-protected areas of the website.",
            "D) Enabling logging for specific virtual hosts."
        ],
        "answer": "A",
        "reason": "Coyote is Tomcat's connector component. It handles external communication, including connection settings such as the maximum number of simultaneous request-handling threads."
    },
    {
        "question": "The Domain Name Service is critical for mapping human-readable names to IP addresses. Why does DNS primarily use UDP on port 53 rather than TCP?",
        "options": [
            "A) UDP provides higher security and data encryption.",
            "B) UDP is faster for short, single-packet name-to-IP queries.",
            "C) UDP guarantees that every request will be eventually delivered.",
            "D) TCP is incapable of handling port 53 communications."
        ],
        "answer": "B",
        "reason": "DNS lookups are usually small and quick. UDP avoids the overhead of setting up a TCP connection, making it faster for short name-resolution queries."
    },
    {
        "question": "Security standards have evolved significantly since 2007. According to the 2026 update, what is the current industry stance regarding plain HTTP, meaning unencrypted websites?",
        "options": [
            "A) They are recommended for faster performance on mobile devices.",
            "B) They are still the standard for all non-banking information.",
            "C) Browsers now flag them as Not secure to warn the user.",
            "D) They are no longer supported by any modern DNS providers."
        ],
        "answer": "C",
        "reason": "Plain HTTP does not encrypt traffic. Modern browsers warn users by marking these sites as Not secure."
    },
    {
        "question": "The HTTP HEAD method is often used by caches and crawlers. What is the defining characteristic of a response to a HEAD request?",
        "options": [
            "A) It returns only the body of the resource to save header space.",
            "B) It returns a 404 error if the resource is too large to process.",
            "C) It returns the same headers as a GET request but with no message body.",
            "D) It forces the server to delete the resource after the headers are sent."
        ],
        "answer": "C",
        "reason": "HEAD is like GET, but the server only sends the response headers. It does not send the actual response body."
    },
    {
        "question": "Modern front-end development often uses meta-frameworks like Next.js or Nuxt. What is a primary reason for using these instead of a basic library like React or Vue?",
        "options": [
            "A) They are the only way to write valid HTML5 code.",
            "B) They provide built-in Server-Side Rendering (SSR) and routing.",
            "C) They allow the browser to run without a TCP/IP connection.",
            "D) They replace the need for JavaScript in the browser."
        ],
        "answer": "B",
        "reason": "Meta-frameworks such as Next.js and Nuxt add features like routing, Server-Side Rendering, and project structure on top of base libraries like React or Vue."
    },
    {
        "question": "Character sets are essential for displaying global content. Which encoding is currently the Web default because it is variable-length and backward-compatible with ASCII?",
        "options": [
            "A) ISO-8859-1 (Latin-1)",
            "B) UTF-16",
            "C) US-ASCII (7-bit)",
            "D) UTF-8"
        ],
        "answer": "D",
        "reason": "UTF-8 is the modern web default because it supports many characters, uses variable-length encoding, and remains backward-compatible with ASCII."
    },
    {
        "question": "Virtual Hosting allows a single physical server with one IP address to host hundreds of different websites. How does the server know which specific website to serve when a request arrives?",
        "options": [
            "A) By checking the source IP address of the client.",
            "B) By assigning a different UDP port to every website.",
            "C) By reading the Host header provided in the HTTP request.",
            "D) By analyzing the Accept-Language header."
        ],
        "answer": "C",
        "reason": "The Host header tells the server which domain the client is requesting. This allows one server and one IP address to host multiple websites."
    },
    {
        "question": "APIs have shifted from simple form-posts to complex data exchanges. What is a key advantage of GraphQL compared to traditional REST APIs?",
        "options": [
            "A) It requires no server-side processing to function.",
            "B) It is limited to binary data for maximum security.",
            "C) It allows the client to request only the specific fields needed.",
            "D) It only works over the older HTTP/1.0 protocol."
        ],
        "answer": "C",
        "reason": "GraphQL lets the client specify exactly which fields it wants. This can reduce over-fetching and under-fetching compared to some REST APIs."
    },
    {
        "question": "For real-time applications like live sports updates or chat systems, which technology provides a persistent, bidirectional connection between the client and server?",
        "options": [
            "A) RESTful GET requests",
            "B) WebSockets",
            "C) Server-Side Rendering (SSR)",
            "D) Static Site Generation (SSG)"
        ],
        "answer": "B",
        "reason": "WebSockets keep a persistent connection open between the client and server. This allows both sides to send messages in real time."
    },
    {
        "question": "In the structure of an HTTP/1.1 Request Message, which header is mandatory to include for the request to be considered valid?",
        "options": [
            "A) User-Agent",
            "B) Host",
            "C) Referer",
            "D) Content-Length"
        ],
        "answer": "B",
        "reason": "HTTP/1.1 requires the Host header because it identifies which website or virtual host the client wants to access."
    },
    {
        "question": "In the 2026 update, TLS 1.3 is highlighted for its performance benefits. What does 1-RTT or 0-RTT refer to in the context of secure connections?",
        "options": [
            "A) The number of physical cables required for the connection.",
            "B) The total number of errors allowed before a connection drops.",
            "C) The number of round-trips required to complete a handshake.",
            "D) The version of the IP protocol being used."
        ],
        "answer": "C",
        "reason": "RTT means round-trip time. In TLS handshakes, 1-RTT or 0-RTT describes how many back-and-forth communication rounds are needed before secure data can be sent."
    },
    {
        "question": "Modern DevOps practices include Infrastructure as Code. What is the primary goal of using IaC tools like Terraform in web development?",
        "options": [
            "A) To automatically write the CSS for a website.",
            "B) To replace the need for human developers in the build process.",
            "C) To manage and deploy servers and networks using configuration files.",
            "D) To encrypt the message body of every HTTP request."
        ],
        "answer": "C",
        "reason": "Infrastructure as Code lets teams define servers, networks, and cloud resources using configuration files. This makes deployment more repeatable and easier to manage."
    },
    {
        "question": "Which modern browser capability allows for native-speed execution of code written in languages like C++ or Rust, enabling complex apps like Photoshop to run in the web browser?",
        "options": [
            "A) JavaScript ES2024",
            "B) WebAssembly (Wasm)",
            "C) CSS Flexbox",
            "D) HTML5 Semantic Tags"
        ],
        "answer": "B",
        "reason": "WebAssembly allows code written in languages like C++ or Rust to run in the browser at near-native speed, making complex web applications possible."
    },
    {
        "question": "What is the main purpose of HTML markup?",
        "options": [
            "A) To make every web page look the same.",
            "B) To describe document structure and meaning.",
            "C) To store private data inside the page.",
            "D) To replace browsers with static files."
        ],
        "answer": "B",
        "reason": "HTML markup is mainly used to describe the structure and meaning of a document. It tells the browser what parts of the page are headings, paragraphs, links, images, lists, and other content."
    },
    {
        "question": "What does the browser mainly do with HTML markup?",
        "options": [
            "A) It permanently changes the source file.",
            "B) It converts all elements into images.",
            "C) It renders the structured document.",
            "D) It removes all attributes before display."
        ],
        "answer": "C",
        "reason": "The browser reads the HTML markup and renders the structured document visually for the user. It does not permanently change the original HTML source file."
    },
    {
        "question": "In HTML, a document can be understood as what kind of structure?",
        "options": [
            "A) A flat list of isolated commands.",
            "B) A tree of elements and text.",
            "C) A database with rows only.",
            "D) A collection of CSS declarations."
        ],
        "answer": "B",
        "reason": "An HTML document is represented as a tree structure, often called the DOM tree. Elements can contain text and other elements, creating parent-child relationships."
    },
    {
        "question": "Why did XHTML introduce stricter authoring rules?",
        "options": [
            "A) To remove support for web images.",
            "B) To make CSS unnecessary.",
            "C) To make parsing more consistent.",
            "D) To force all pages to use frames."
        ],
        "answer": "C",
        "reason": "XHTML introduced stricter rules so that documents could be parsed more consistently. Proper closing tags, correct nesting, and lowercase elements help reduce ambiguity."
    },
    {
        "question": "Which example shows correct XHTML-style nesting?",
        "options": [
            "A) <p>Hello <strong>class</p></strong>",
            "B) <p>Hello <strong>class</strong></p>",
            "C) <p><strong>Hello</p> class</strong>",
            "D) <strong><p>Hello</strong></p>"
        ],
        "answer": "B",
        "reason": "Correct XHTML-style nesting means the last tag opened must be the first tag closed. In option B, <strong> is opened inside <p> and closed before </p>."
    },
    {
        "question": "What is the role of a document type declaration?",
        "options": [
            "A) It adds a visible title to the page.",
            "B) It defines the visual color theme.",
            "C) It tells validators which grammar to use.",
            "D) It prevents links from being used."
        ],
        "answer": "C",
        "reason": "A document type declaration tells validators and browsers what document rules or grammar the page is expected to follow."
    },
    {
        "question": "In normal HTML rendering, what usually happens to extra spaces?",
        "options": [
            "A) They are always preserved exactly.",
            "B) They are collapsed into one space.",
            "C) They automatically create tables.",
            "D) They make the document invalid."
        ],
        "answer": "B",
        "reason": "In normal HTML rendering, multiple spaces, tabs, or line breaks are usually collapsed into a single space. This is why extra spacing in HTML source code does not usually appear on the page."
    },
    {
        "question": "Which element is used when spacing must be preserved?",
        "options": [
            "A) <span>",
            "B) <pre>",
            "C) <strong>",
            "D) <title>"
        ],
        "answer": "B",
        "reason": "The <pre> element preserves whitespace and line breaks exactly as written. It is useful for code blocks or text where spacing matters."
    },
    {
        "question": "Why are character entities such as &lt; useful?",
        "options": [
            "A) They create hidden browser comments.",
            "B) They validate all links automatically.",
            "C) They display special characters safely.",
            "D) They replace the need for attributes."
        ],
        "answer": "C",
        "reason": "Character entities allow special characters to be displayed safely. For example, &lt; displays the less-than symbol without the browser treating it as the start of an HTML tag."
    },
    {
        "question": "What does the href attribute usually specify in an <a> element?",
        "options": [
            "A) The font size of the link.",
            "B) The destination URL of the link.",
            "C) The heading level of the page.",
            "D) The table header of a column."
        ],
        "answer": "B",
        "reason": "The href attribute in an <a> element specifies the destination URL where the link should take the user."
    },
    {
        "question": "Which element is best for marking important text semantically?",
        "options": [
            "A) <br>",
            "B) <strong>",
            "C) <table>",
            "D) <frameset>"
        ],
        "answer": "B",
        "reason": "The <strong> element marks text as important semantically. It usually appears bold in browsers, but its main purpose is meaning, not just appearance."
    },
    {
        "question": "What is a good practice when writing link text?",
        "options": [
            "A) Use “click here” for all links.",
            "B) Leave the anchor text empty.",
            "C) Name the destination clearly.",
            "D) Use numbers as link labels."
        ],
        "answer": "C",
        "reason": "Good link text should clearly describe the destination. This helps users understand where the link goes and improves accessibility."
    },
    {
        "question": "What should the alt attribute of an image provide?",
        "options": [
            "A) A CSS class for the image.",
            "B) Alternative text for the image.",
            "C) The exact image file size.",
            "D) A password for loading images."
        ],
        "answer": "B",
        "reason": "The alt attribute provides alternative text for an image. This helps screen readers and also gives information if the image fails to load."
    },
    {
        "question": "Why should comments not contain secrets?",
        "options": [
            "A) Comments are shown as headings.",
            "B) Comments are visible in source.",
            "C) Comments become form fields.",
            "D) Comments submit data automatically."
        ],
        "answer": "B",
        "reason": "HTML comments are not displayed on the page, but they are still visible in the page source. Therefore, passwords, private notes, or secret information should never be placed in comments."
    },
    {
        "question": "What does the “last opened, first closed” idea describe?",
        "options": [
            "A) Browser color selection.",
            "B) Correct nesting of tags.",
            "C) HTTP method selection.",
            "D) Image dimension calculation."
        ],
        "answer": "B",
        "reason": "The “last opened, first closed” rule describes correct tag nesting. If one element is opened inside another, the inner element must be closed first."
    },
    {
        "question": "Which list type is appropriate when the order of items matters?",
        "options": [
            "A) <ul>",
            "B) <ol>",
            "C) <dl>",
            "D) <table>"
        ],
        "answer": "B",
        "reason": "The <ol> element creates an ordered list. It is appropriate when sequence matters, such as steps in a process or ranked items."
    },
    {
        "question": "What are HTML tables mainly intended for?",
        "options": [
            "A) Creating all page layouts.",
            "B) Showing row-column relationships.",
            "C) Replacing forms and links.",
            "D) Defining browser settings."
        ],
        "answer": "B",
        "reason": "HTML tables are mainly intended for tabular data, where information has row-column relationships. They should not be used as the main tool for page layout."
    },
    {
        "question": "In a form, what is the purpose of the name attribute on an input?",
        "options": [
            "A) It defines the browser title.",
            "B) It names submitted form data.",
            "C) It changes the document type.",
            "D) It makes the input invisible."
        ],
        "answer": "B",
        "reason": "The name attribute identifies the form data when it is submitted. The server uses the name as the key for the submitted value."
    },
    {
        "question": "What is a key difference between GET and POST in forms?",
        "options": [
            "A) GET encrypts data automatically.",
            "B) POST works only with images.",
            "C) GET sends data in the URL.",
            "D) GET removes the need for servers."
        ],
        "answer": "C",
        "reason": "GET sends form data in the URL as query parameters. POST sends data in the request body, which is usually better for larger or more sensitive form submissions."
    },
    {
        "question": "What is the durable lesson of Chapter 2?",
        "options": [
            "A) XHTML should replace all HTML.",
            "B) Frames should organize all pages.",
            "C) Disciplined structure matters.",
            "D) CSS should be inside every tag."
        ],
        "answer": "C",
        "reason": "The durable lesson is that disciplined structure matters. Well-structured markup is easier to read, validate, maintain, and render correctly."
    },
    {
        "question": "Of the three CSS integration methods, which has the highest specificity contribution?",
        "options": [
            "A) External stylesheet linked from the HTML head section",
            "B) Internal styles placed in a style block in the head",
            "C) Inline style attribute applied directly to the element",
            "D) Browser user-agent default rules for the element type"
        ],
        "answer": "C",
        "reason": "Inline styles have the highest specificity contribution because they are applied directly to the element using the style attribute."
    },
    {
        "question": "How is an external CSS file linked to an HTML document?",
        "options": [
            "A) <style src=\"style.css\"></style> inside the body",
            "B) <link rel=\"stylesheet\" href=\"style.css\"> in the head",
            "C) <import file=\"style.css\" /> at the top of the file",
            "D) <css href=\"style.css\" type=\"text/css\"> in the head"
        ],
        "answer": "B",
        "reason": "An external CSS file is linked with a <link> element inside the HTML head. The rel attribute identifies it as a stylesheet, and href gives the file path."
    },
    {
        "question": "What does the selector p { color: gray; } match?",
        "options": [
            "A) Every <p> element in the entire document",
            "B) Only the first <p> element on the page",
            "C) Only <p> elements that carry a class or id",
            "D) Only <p> elements nested directly inside body"
        ],
        "answer": "A",
        "reason": "The selector p is an element selector. It matches every paragraph element in the document."
    },
    {
        "question": "What prefix is used to select an element by its class attribute?",
        "options": [
            "A) The hash symbol # before the name",
            "B) The colon symbol : before the name",
            "C) The at-sign symbol @ before the name",
            "D) The dot symbol . before the name"
        ],
        "answer": "D",
        "reason": "Class selectors use a dot before the class name. For example, .menu selects elements with class=\"menu\"."
    },
    {
        "question": "Which statement about ID selectors is correct?",
        "options": [
            "A) An ID may be reused for any number of sibling elements",
            "B) An ID has lower specificity than any class selector",
            "C) An ID should identify exactly one unique element per page",
            "D) An ID can only be used to style form input elements"
        ],
        "answer": "C",
        "reason": "An ID is meant to identify one unique element on a page. Reusing the same ID for multiple elements is invalid and can cause styling or JavaScript problems."
    },
    {
        "question": "When two rules have the same specificity, how does the cascade decide the winner?",
        "options": [
            "A) The rule that appears later in the stylesheet wins",
            "B) The rule that appears earlier in the stylesheet wins",
            "C) The browser averages the conflicting property values",
            "D) The browser picks one rule at random per page load"
        ],
        "answer": "A",
        "reason": "When specificity is equal, source order decides. The rule written later in the stylesheet overrides the earlier one."
    },
    {
        "question": "What is the correct order of the four cascade criteria?",
        "options": [
            "A) origin, source order, specificity, importance",
            "B) specificity, origin, importance, source order",
            "C) origin, importance, specificity, source order",
            "D) importance, source order, specificity, origin"
        ],
        "answer": "C",
        "reason": "The cascade first considers origin, then importance, then specificity, and finally source order when earlier criteria are tied."
    },
    {
        "question": "In the specificity tuple (a, b, c, d), what does position a count?",
        "options": [
            "A) Inline styles set via the style attribute",
            "B) IDs introduced in the stylesheet with #",
            "C) Classes, attributes, and pseudo-classes together",
            "D) Element types and pseudo-elements together"
        ],
        "answer": "A",
        "reason": "In the specificity tuple, position a counts inline styles. Inline styles have stronger weight than ID, class, and element selectors."
    },
    {
        "question": "What is the specificity of the selector #nav .item a?",
        "options": [
            "A) (0, 0, 1, 2)",
            "B) (0, 1, 1, 1)",
            "C) (0, 1, 2, 0)",
            "D) (1, 1, 0, 1)"
        ],
        "answer": "B",
        "reason": "#nav contributes one ID, .item contributes one class, and a contributes one element selector. There is no inline style, so the specificity is (0, 1, 1, 1)."
    },
    {
        "question": "How are two specificity tuples compared to pick a winner?",
        "options": [
            "A) By computing the sum of all four positions",
            "B) By comparing positions from right to left",
            "C) By taking the average of the four positions",
            "D) By comparing positions from left to right"
        ],
        "answer": "D",
        "reason": "Specificity tuples are compared from left to right. The first larger value determines which selector is more specific."
    },
    {
        "question": "What is the effect of adding !important to a declaration?",
        "options": [
            "A) It adds 1 to position a of the specificity tuple",
            "B) It doubles the specificity score for that rule",
            "C) It lifts the declaration into a higher cascade bucket",
            "D) It triggers the rule before any selector matches"
        ],
        "answer": "C",
        "reason": "!important changes the cascade priority by placing the declaration in a higher importance bucket. It does not simply add to the specificity number."
    },
    {
        "question": "Which CSS property is naturally inherited by descendants?",
        "options": [
            "A) The background color from the parent element",
            "B) The text color from the parent element",
            "C) The border width from the parent element",
            "D) The element width from the parent element"
        ],
        "answer": "B",
        "reason": "The color property is naturally inherited, so child elements usually inherit the text color of their parent unless another color is set."
    },
    {
        "question": "Which property does NOT inherit by default from parent to children?",
        "options": [
            "A) The background-color property is not inherited",
            "B) The text color property is not inherited",
            "C) The font-family property is not inherited",
            "D) The line-height property is not inherited"
        ],
        "answer": "A",
        "reason": "background-color does not inherit by default. A child may appear to have the same background only because its own background is transparent."
    },
    {
        "question": "What does text-align: center do?",
        "options": [
            "A) It centers a block element inside its parent container",
            "B) It vertically centers text within the element's height",
            "C) It centers an image relative to surrounding text",
            "D) It centers inline content within the element's box"
        ],
        "answer": "D",
        "reason": "text-align: center centers inline content, such as text and inline elements, inside the element's box. It does not automatically center the block element itself."
    },
    {
        "question": "Which line correctly describes color and background-color?",
        "options": [
            "A) color sets the background; background-color sets the text color",
            "B) color and background-color name the same underlying property",
            "C) color affects borders only; background-color affects the fill",
            "D) color sets the text color; background-color sets the fill area"
        ],
        "answer": "D",
        "reason": "The color property controls text color, while background-color controls the fill area behind the content."
    },
    {
        "question": "How is the px unit best described?",
        "options": [
            "A) Relative to the parent element's font-size at compute time",
            "B) An absolute unit with the same size regardless of context",
            "C) Relative to the viewport width at the current zoom level",
            "D) Relative to the html root font-size for accessibility"
        ],
        "answer": "B",
        "reason": "px is treated as an absolute CSS unit. Unlike em, rem, vh, or %, it does not depend on parent font size or viewport dimensions."
    },
    {
        "question": "How do em and rem differ?",
        "options": [
            "A) em is absolute; rem is relative to the viewport height",
            "B) em and rem are exact aliases kept for legacy reasons",
            "C) em is relative to parent font-size; rem is relative to html",
            "D) em is relative to html; rem is relative to the parent element"
        ],
        "answer": "C",
        "reason": "em is relative to the font size of the parent or current context, while rem is relative to the root html element's font size."
    },
    {
        "question": "What does 1vh represent in CSS?",
        "options": [
            "A) 1% of the browser viewport height",
            "B) 1% of the parent element's own height",
            "C) 1 pixel multiplied by screen density",
            "D) 1% of the document body height"
        ],
        "answer": "A",
        "reason": "vh stands for viewport height. Therefore, 1vh equals 1% of the browser viewport height."
    },
    {
        "question": "Which calc() expression is syntactically valid?",
        "options": [
            "A) calc(100%-20px) with no spaces between operands",
            "B) calc(100% -20px) with a space before but not after",
            "C) calc(100% - 20px) with spaces around the minus",
            "D) calc(100% -- 20px) with a doubled minus operator"
        ],
        "answer": "C",
        "reason": "In calc(), the plus and minus operators need spaces around them. Therefore, calc(100% - 20px) is the valid expression."
    },
    {
        "question": "In the box model, what is the order from inside to outside?",
        "options": [
            "A) margin, border, padding, content",
            "B) padding, content, margin, border",
            "C) content, margin, padding, border",
            "D) content, padding, border, margin"
        ],
        "answer": "D",
        "reason": "The CSS box model starts with the content area, then padding, then border, and finally margin on the outside."
    },
    {
        "question": "Without box-sizing, what does width: 300px set?",
        "options": [
            "A) The total visible width including padding and border",
            "B) The content area only; padding and border add on top",
            "C) The content plus padding only; border is added on top",
            "D) The outer dimension including the surrounding margin"
        ],
        "answer": "B",
        "reason": "By default, width applies only to the content area. Padding and border are added outside that width, making the visible box larger."
    },
    {
        "question": "What is the effect of box-sizing: border-box?",
        "options": [
            "A) The border is removed from the visible rendering of the box",
            "B) Padding and border are excluded entirely from the layout",
            "C) The element width refers to the parent container instead",
            "D) The width includes content, padding, and border together"
        ],
        "answer": "D",
        "reason": "With box-sizing: border-box, the declared width includes the content, padding, and border. This makes layout sizing easier to predict."
    },
    {
        "question": "How is margin defined in the CSS box model?",
        "options": [
            "A) Transparent space placed between content and the border",
            "B) Coloured space drawn with the element's background color",
            "C) Coloured space placed inside the border on each side",
            "D) Transparent space placed outside the border from neighbours"
        ],
        "answer": "D",
        "reason": "Margin is transparent space outside the border. It separates an element from neighbouring elements."
    },
    {
        "question": "Which describes the :hover pseudo-class?",
        "options": [
            "A) A virtual child element generated above the matched element",
            "B) A state that matches while the pointer is over the element",
            "C) A state that matches once the user has clicked the element",
            "D) A media query that only activates on devices with a mouse"
        ],
        "answer": "B",
        "reason": ":hover applies when the user's pointer is over the element. It is commonly used for buttons, links, and interactive visual feedback."
    },
    {
        "question": "What does the selector A > B match?",
        "options": [
            "A) B elements that are direct children of an A element",
            "B) B elements nested anywhere inside an A element",
            "C) B elements that are the next sibling of an A element",
            "D) B elements appearing before A in the document order"
        ],
        "answer": "A",
        "reason": "The > combinator selects only direct children. A > B matches B elements whose immediate parent is A."
    },
    {
        "question": "What does the descendant combinator A B select?",
        "options": [
            "A) B elements that are direct children of A only",
            "B) B elements that are immediately preceded by A",
            "C) B elements nested anywhere inside A, at any depth",
            "D) A elements that contain at least one B descendant"
        ],
        "answer": "C",
        "reason": "The descendant combinator selects matching elements at any depth inside the ancestor. A B selects B elements anywhere inside A."
    },
    {
        "question": "What does the group selector h1, h2, p do?",
        "options": [
            "A) Applies the same declarations to h1, h2, and p elements",
            "B) Selects only h1 elements followed by h2 followed by p",
            "C) Selects the first occurrence of any of h1, h2, or p",
            "D) Applies the rule only when h1, h2, and p are siblings"
        ],
        "answer": "A",
        "reason": "Commas group selectors together. h1, h2, p applies the same CSS declarations to all h1 elements, h2 elements, and p elements."
    },
    {
        "question": "What does the universal selector * match?",
        "options": [
            "A) Elements without any class, id, or attribute selectors",
            "B) Elements directly inside the body of the document",
            "C) Every element in the document, regardless of type",
            "D) The root element of the page and its immediate children"
        ],
        "answer": "C",
        "reason": "The universal selector * matches every element in the document, regardless of tag name, class, id, or attribute."
    },
    {
        "question": "Which elements does a[href^=\"https\"] match?",
        "options": [
            "A) Anchors whose href ends with \"https\"",
            "B) Anchors whose href contains \"https\" anywhere",
            "C) Anchors whose href exactly equals \"https\"",
            "D) Anchors whose href starts with \"https\""
        ],
        "answer": "D",
        "reason": "The ^= attribute selector means 'starts with'. Therefore, a[href^=\"https\"] matches anchor elements whose href value starts with https."
    },
    {
        "question": "What does the selector h2 + p match?",
        "options": [
            "A) Every p that appears anywhere after an h2 sibling",
            "B) Every p that comes before an h2 in the same parent",
            "C) Every p that is nested directly inside an h2 element",
            "D) The first p immediately after each h2 at the same level"
        ],
        "answer": "D",
        "reason": "The + combinator selects the immediately following sibling. h2 + p matches a p element that comes directly after an h2 at the same level."
    },
    {
        "question": "What does the selector li:nth-child(odd) target?",
        "options": [
            "A) li elements at odd positions, such as 1st, 3rd, and 5th, among siblings",
            "B) li elements whose class name contains the word odd",
            "C) li elements where the total sibling count is an odd number",
            "D) li elements that are children of an element with id odd"
        ],
        "answer": "A",
        "reason": "nth-child(odd) selects elements in odd-numbered positions among their siblings, such as the 1st, 3rd, and 5th items."
    },
    {
        "question": "What does the selector :not(.active) match?",
        "options": [
            "A) Elements that come right after a .active element",
            "B) Elements that do not carry the .active class on them",
            "C) Elements placed before .active in document order",
            "D) Elements that remove .active from their class list"
        ],
        "answer": "B",
        "reason": ":not(.active) matches elements that do not have the active class. It is useful for excluding certain elements from a rule."
    },
    {
        "question": "Which statement about ::before is correct?",
        "options": [
            "A) It selects the element placed just before the matched one",
            "B) It triggers a rule only before the page finishes loading",
            "C) It generates a virtual child at the start of the element",
            "D) It inserts a real sibling tag before the matched element"
        ],
        "answer": "C",
        "reason": "::before creates generated content at the beginning of the selected element. It is not a real HTML tag, but a CSS-generated pseudo-element."
    },
    {
        "question": "How are CSS custom properties, also called variables, declared and read?",
        "options": [
            "A) Declared with var(--name); read with the -- prefix in values",
            "B) Declared with the -- prefix; read with the var(--name) function",
            "C) Declared with the @var rule; read with the @ symbol in values",
            "D) Declared inside @media; read only within that same query"
        ],
        "answer": "B",
        "reason": "CSS custom properties are declared using the -- prefix, such as --main-color. They are read using the var() function, such as var(--main-color)."
    },
    {
        "question": "Which is an accessibility best practice for focused elements?",
        "options": [
            "A) Set outline: none everywhere to keep the design clean",
            "B) Use a hover effect instead, since mouse users dominate",
            "C) Replace the focus outline with cursor: pointer for clarity",
            "D) Preserve a visible focus indicator so keyboard users see it"
        ],
        "answer": "D",
        "reason": "A visible focus indicator helps keyboard users know which element is currently selected. Removing focus outlines without a replacement hurts accessibility."
    },
    {
        "question": "What is the default value of the position property for all HTML elements in standard CSS?",
        "options": [
            "A) relative",
            "B) absolute",
            "C) static",
            "D) fixed"
        ],
        "answer": "C",
        "reason": "The default position value for HTML elements is static. This means elements appear in the normal document flow unless another position value is applied."
    },
    {
        "question": "When applying position: relative to an element, how does the browser calculate its final rendered location?",
        "options": [
            "A) It positions the element relative to its nearest positioned ancestor.",
            "B) It positions the element relative to the initial containing viewport.",
            "C) It shifts the element from its normal place without moving its neighbors.",
            "D) It moves the element directly to the top-left corner of the page."
        ],
        "answer": "C",
        "reason": "position: relative keeps the element in the normal flow, then visually shifts it from where it would normally be. Neighboring elements still behave as if it stayed in its original place."
    },
    {
        "question": "Which CSS positioning property removes an element entirely from the normal document flow and positions it relative to its nearest ancestor that has a position value other than static?",
        "options": [
            "A) position: absolute",
            "B) position: relative",
            "C) position: static",
            "D) position: sticky"
        ],
        "answer": "A",
        "reason": "position: absolute removes the element from the normal document flow. It is positioned relative to the nearest positioned ancestor, meaning an ancestor whose position is not static."
    },
    {
        "question": "If an element inside a webpage layout is given the property position: absolute, what happens to the space it originally occupied in the normal flow?",
        "options": [
            "A) The original space remains reserved and neighbor elements stay in place.",
            "B) The original space expands dynamically to fill the container's width.",
            "C) The element is removed from the flow and neighbor elements reflow into its space.",
            "D) The original space is duplicated directly below the parent element."
        ],
        "answer": "C",
        "reason": "An absolutely positioned element is removed from the normal flow. Because its original space is no longer reserved, nearby elements can move into that space."
    },
    {
        "question": "Which CSS positioning property should be used to anchor a navigation header to the top of the browser viewport so that it remains visible in the exact same spot while the user scrolls down the page?",
        "options": [
            "A) position: relative",
            "B) position: absolute",
            "C) position: sticky",
            "D) position: fixed"
        ],
        "answer": "D",
        "reason": "position: fixed attaches an element to the browser viewport. It stays in the same visible location even when the user scrolls."
    },
    {
        "question": "How does an element configured with position: sticky behave before it reaches the specified scroll threshold within its parent container?",
        "options": [
            "A) It behaves exactly like a fixed element.",
            "B) It behaves exactly like a relative element.",
            "C) It behaves exactly like an absolute element.",
            "D) It remains completely hidden from the user view."
        ],
        "answer": "B",
        "reason": "Before reaching its scroll threshold, a sticky element behaves like a relatively positioned element. After the threshold is reached, it sticks within its container."
    },
    {
        "question": "Which of the following sets of values represents all the valid core directions accepted by the flex-direction property?",
        "options": [
            "A) row, row-reverse, column, column-reverse",
            "B) horizontal, vertical, standard, reverse",
            "C) left, right, top, bottom",
            "D) start, end, center, stretch"
        ],
        "answer": "A",
        "reason": "The core values for flex-direction are row, row-reverse, column, and column-reverse. These control the direction of the flex container's main axis."
    },
    {
        "question": "What is the default layout direction of the main axis when a container is initialized using display: flex?",
        "options": [
            "A) column",
            "B) row",
            "C) grid",
            "D) block"
        ],
        "answer": "B",
        "reason": "The default flex-direction is row. This means flex items are laid out horizontally along the main axis by default."
    },
    {
        "question": "Which CSS Flexbox property is explicitly used by developers to distribute alignment and extra space among flex items along the horizontal main axis of a row container?",
        "options": [
            "A) align-items",
            "B) align-content",
            "C) justify-content",
            "D) flex-wrap"
        ],
        "answer": "C",
        "reason": "In a row flex container, the main axis is horizontal. justify-content controls how items and extra space are distributed along that main axis."
    },
    {
        "question": "When styling a flex container, what specific distribution effect is achieved by applying the utility value justify-content: space-between?",
        "options": [
            "A) It adds an equal amount of padding around the outer edges of all items.",
            "B) It distributes leftover space equally between items, leaving none at the edges.",
            "C) It centers all items together and adds a fixed margin between them.",
            "D) It forces items to stretch vertically to fill the entire cross axis."
        ],
        "answer": "B",
        "reason": "justify-content: space-between places the first item at the start and the last item at the end, then distributes leftover space evenly between the items."
    },
    {
        "question": "Which CSS Flexbox property is designed to control how individual layout items are aligned and positioned along the perpendicular cross axis inside a container?",
        "options": [
            "A) justify-content",
            "B) flex-direction",
            "C) flex-grow",
            "D) align-items"
        ],
        "answer": "D",
        "reason": "align-items controls alignment along the cross axis, which is perpendicular to the main axis in a flex container."
    },
    {
        "question": "If a developer sets up a flex row container that is 200 pixels tall but does not explicitly specify a value for the align-items property, how will child items of varying heights behave?",
        "options": [
            "A) They will align to the vertical center of the container.",
            "B) They will align to the top edge of the container.",
            "C) They will stretch vertically to fill the cross-axis size.",
            "D) They will align their text baselines automatically."
        ],
        "answer": "C",
        "reason": "The default value of align-items is stretch. In a row flex container, this causes items to stretch vertically along the cross axis when possible."
    },
    {
        "question": "When the property flex-direction: column is added to a flex container, how are the layout responsibilities of the alignment properties altered?",
        "options": [
            "A) justify-content controls vertical placement, and align-items controls horizontal placement.",
            "B) justify-content controls horizontal placement, and align-items controls vertical placement.",
            "C) Both justify-content and align-items control horizontal alignment simultaneously.",
            "D) Both justify-content and align-items control vertical alignment simultaneously."
        ],
        "answer": "A",
        "reason": "With flex-direction: column, the main axis becomes vertical. Therefore, justify-content controls vertical placement, while align-items controls horizontal placement on the cross axis."
    },
    {
        "question": "What is the default layout behavior of a flex container when the combined width of its child items exceeds the total available width of the main axis line?",
        "options": [
            "A) The container wraps items onto multiple new lines automatically.",
            "B) The container clips and hides the overflowing items implicitly.",
            "C) The items shrink or overflow on a single continuous line.",
            "D) The items convert into a two-dimensional grid format."
        ],
        "answer": "C",
        "reason": "By default, flex-wrap is nowrap. This means items remain on one line and may shrink or overflow rather than automatically wrapping."
    },
    {
        "question": "In modern CSS development, the shorthand property declaration flex: 1 is equivalent to which combination of individual flex properties?",
        "options": [
            "A) flex-direction: row; flex-wrap: wrap; gap: 1px;",
            "B) flex-grow: 1; flex-shrink: 1; flex-basis: 0;",
            "C) grid-template-columns: repeat(1, 1fr);",
            "D) position: relative; top: 0; left: 0;"
        ],
        "answer": "B",
        "reason": "flex: 1 is commonly interpreted as flex-grow: 1, flex-shrink: 1, and flex-basis: 0. This allows flex items to share available space evenly."
    },
    {
        "question": "If a child element inside a horizontal flex row retains the default factor of flex-grow: 0, how does it respond to extra unallocated space along the main axis line?",
        "options": [
            "A) The item shrinks proportionally to make room for its surrounding neighbors.",
            "B) The item expands dynamically to capture all remaining leftover space.",
            "C) The item remains at its natural size based on its explicit width or content.",
            "D) The item is compressed and becomes completely invisible on the layout."
        ],
        "answer": "C",
        "reason": "With flex-grow: 0, the item does not expand to take leftover space. It stays at its natural size or its explicitly defined size."
    },
    {
        "question": "Which modern native CSS layout system is explicitly engineered to handle complex web interfaces requiring two-dimensional alignment across both simultaneous rows and columns?",
        "options": [
            "A) Absolute Positioning Layout",
            "B) Flexbox Layout System",
            "C) Grid Layout System",
            "D) Block Flow Layout Model"
        ],
        "answer": "C",
        "reason": "CSS Grid is designed for two-dimensional layouts. It controls both rows and columns at the same time, making it ideal for complex page structures."
    },
    {
        "question": "When setting up a multi-column track definition using CSS Grid, what does the fractional unit measure 1fr explicitly represent to the browser?",
        "options": [
            "A) One fraction of the remaining free space left after fixed tracks are allocated.",
            "B) One physical pixel calculated relative to the mobile hardware viewport screen.",
            "C) One percent of the parent container absolute maximum total computed width.",
            "D) One typography unit measured relative to the root element default font size."
        ],
        "answer": "A",
        "reason": "In CSS Grid, 1fr means one fraction of the remaining available space after fixed-size tracks have been calculated."
    },
    {
        "question": "When building interfaces with Flexbox or Grid layouts, where does the shorthand layout property gap insert spacing?",
        "options": [
            "A) On the outer boundaries of the container element only.",
            "B) Around all four individual sides of every single child element.",
            "C) Exclusively between the adjacent layout tracks or internal items.",
            "D) Between the outer border edge and the internal content bounding box."
        ],
        "answer": "C",
        "reason": "The gap property adds spacing between grid or flex items. It does not add outside margin around the container or around every side of each item."
    },
    {
        "question": "If a specific child item inside a CSS Grid container is assigned the property rule grid-column: span 2, what layout behavior will the browser enforce?",
        "options": [
            "A) The grid container will create two additional column tracks globally.",
            "B) The designated grid item will stretch to occupy two column tracks.",
            "C) The designated grid item will copy its content down into two rows.",
            "D) The cell will split its internal text into two isolated side panels."
        ],
        "answer": "B",
        "reason": "grid-column: span 2 makes the selected grid item cover two column tracks. It does not create new global columns by itself."
    },
    {
        "question": "Which explicit property allows developers to map out an entire structural page design containing a header, sidebar, main area, and footer visually using plain English names?",
        "options": [
            "A) grid-template-columns",
            "B) repeat(auto-fit, minmax())",
            "C) grid-template-areas",
            "D) media query breakpoints"
        ],
        "answer": "C",
        "reason": "grid-template-areas allows developers to name areas of a grid layout, such as header, sidebar, main, and footer, making the page structure easier to understand."
    },
    {
        "question": "What structural layout objective is achieved by applying the advanced CSS Grid property rule grid-template-columns: repeat(auto-fit, minmax(180px, 1fr))?",
        "options": [
            "A) It forces every column track to remain frozen at a width of 180 pixels.",
            "B) It mandates a media query breakpoint to change layout columns on mobile.",
            "C) It builds a responsive multi-column grid that adapts without media queries.",
            "D) It caps the absolute maximum size of the outer grid container to 180 pixels."
        ],
        "answer": "C",
        "reason": "repeat(auto-fit, minmax(180px, 1fr)) creates responsive columns that adapt to available space. It allows the grid to change column count without needing a media query."
    },
    {
        "question": "Why is including the <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> HTML tag considered a mandatory first step for modern responsive web development?",
        "options": [
            "A) It prevents mobile browsers from rendering at a generic desktop width and zooming out.",
            "B) It automatically increases the pixel font size of paragraphs on small viewports.",
            "C) It enables developers to use absolute positioning relative to structural grid tracks.",
            "D) It instructs the rendering engine to download external layout sheets faster."
        ],
        "answer": "A",
        "reason": "The viewport meta tag tells mobile browsers to use the device's actual width. Without it, mobile browsers may render the page as if it were a desktop layout and zoom out."
    },
    {
        "question": "Which CSS rule is utilized by web developers to apply specific blocks of layout styles only when a precise device width condition or media environment is verified as true?",
        "options": [
            "A) @supports",
            "B) @media",
            "C) @keyframes",
            "D) @import"
        ],
        "answer": "B",
        "reason": "@media rules apply CSS only when a media condition is true, such as a viewport width limit or device environment."
    },
    {
        "question": "If a stylesheet includes the responsive condition @media (max-width: 600px) { .box { background: coral; } }, when will the browser render the .box element with a coral background?",
        "options": [
            "A) Only when the viewport width is measured at exactly 600 pixels wide.",
            "B) Whenever the current viewport width is measured at 600 pixels or narrower.",
            "C) Whenever the current viewport width expands to 600 pixels or wider.",
            "D) Only on high-definition device screens that feature a minimum of 600 DPI."
        ],
        "answer": "B",
        "reason": "max-width: 600px means the rule applies when the viewport is 600 pixels wide or smaller."
    },
    {
        "question": "What is the fundamental design workflow philosophy when a developer builds a web application using a strict mobile-first breakpoint strategy?",
        "options": [
            "A) Creating elaborate desktop views first, then hiding crowded layout columns for mobile.",
            "B) Coding simple small-screen styles as the baseline, then layering complexity for large screens.",
            "C) Relying entirely on fluid page width percentages while omitting viewport meta tags.",
            "D) Sizing all interface margins and grids using absolute hardware pixel specs exclusively."
        ],
        "answer": "B",
        "reason": "Mobile-first design starts with simple small-screen styles. Larger-screen features and layout complexity are then added with progressive enhancements."
    },
    {
        "question": "Which specific media query feature is universally relied upon to progressively layer structural layout enhancements as part of a mobile-first responsive architecture?",
        "options": [
            "A) max-width",
            "B) min-width",
            "C) orientation",
            "D) device-pixel-ratio"
        ],
        "answer": "B",
        "reason": "Mobile-first CSS commonly uses min-width queries. The base styles target small screens, and min-width rules add changes as the viewport gets larger."
    },
    {
        "question": "According to industry best practices and core architectural definitions, when should a web developer primarily choose to implement Flexbox over alternative layout options?",
        "options": [
            "A) When items need to be arranged linearly along a single layout axis.",
            "B) When a complex structural grid must control rows and columns together.",
            "C) When elements must be stacked layer by layer using absolute view coordinates.",
            "D) When mapping out the master structural layout wireframes of a website."
        ],
        "answer": "A",
        "reason": "Flexbox is best for one-dimensional layouts, meaning items arranged along a single row or column."
    },
    {
        "question": "According to industry layout guidelines, under what design scenario is it ideal to choose a native CSS Grid system over Flexbox?",
        "options": [
            "A) When organizing a simple, linear single-row horizontal navigation bar.",
            "B) When centering a single block of text content cleanly within a hero banner.",
            "C) When both horizontal rows and vertical columns must be controlled simultaneously.",
            "D) When forcing a single background graphic to stretch fluidly with the window."
        ],
        "answer": "C",
        "reason": "CSS Grid is ideal when the layout requires control over both rows and columns at the same time. Flexbox is better for one-dimensional alignment."
    },
    {
        "question": "If a media query block redefines a class property that matches a default layout property with identical selector specificity, how does the browser resolve the conflict?",
        "options": [
            "A) Properties declared inside a media query automatically have higher default specificity.",
            "B) The media query rules win because they appear later in the cascade order.",
            "C) The matching rules are treated as high-priority inline styles by the browser engine.",
            "D) The media query block bypasses and ignores standard rules of CSS inheritance."
        ],
        "answer": "B",
        "reason": "Media query rules do not automatically have higher specificity. If specificity is equal and the media query appears later, it wins because of normal cascade source order."
    },
    {
        "question": "A student writes the following JavaScript code: console.log(\"Welcome to JavaScript\"); Where will the message appear?",
        "options": [
            "A) In the HTML page title",
            "B) In the browser console",
            "C) In the browser address bar",
            "D) In the CSS stylesheet"
        ],
        "answer": "B",
        "reason": "console.log() prints messages to the browser console. It is mainly used for debugging and checking program output while developing JavaScript."
    },
    {
        "question": "A developer includes this line in an HTML file: <script type=\"module\" src=\"app.js\"></script>. What does type=\"module\" do?",
        "options": [
            "A) It prevents the use of variables",
            "B) It executes the script as CSS",
            "C) It gives the file its own module scope",
            "D) It disables all browser functions"
        ],
        "answer": "C",
        "reason": "A script with type=\"module\" runs as a JavaScript module. Modules have their own scope, so variables declared inside them are not automatically global."
    },
    {
        "question": "Consider the following code: \"use strict\"; total = 100; console.log(total); What will happen?",
        "options": [
            "A) 100 will be printed",
            "B) total will become a global variable",
            "C) An error will occur because total is not declared",
            "D) JavaScript will convert total to undefined"
        ],
        "answer": "C",
        "reason": "In strict mode, JavaScript does not allow assigning a value to an undeclared variable. Since total was not declared with let, const, or var, an error occurs."
    },
    {
        "question": "What will happen in this code? const rate = 0.13; rate = 0.15; console.log(rate);",
        "options": [
            "A) 0.15 will be printed",
            "B) 0.13 will be printed",
            "C) An error will occur because rate cannot be reassigned",
            "D) JavaScript will automatically create a second variable"
        ],
        "answer": "C",
        "reason": "A variable declared with const cannot be reassigned. Trying to assign 0.15 to rate after it was declared causes an error."
    },
    {
        "question": "What will be printed? for (var i = 0; i < 4; i++) { } console.log(i);",
        "options": [
            "A) 0",
            "B) 3",
            "C) 4",
            "D) ReferenceError"
        ],
        "answer": "C",
        "reason": "var is function-scoped, not block-scoped. After the loop finishes, i has been incremented to 4, so console.log(i) prints 4."
    },
    {
        "question": "What will happen in this code? { let score = 90; } console.log(score);",
        "options": [
            "A) 90 will be printed",
            "B) undefined will be printed",
            "C) A ReferenceError will occur",
            "D) null will be printed"
        ],
        "answer": "C",
        "reason": "let is block-scoped. The variable score only exists inside the braces, so trying to access it outside the block causes a ReferenceError."
    },
    {
        "question": "A developer wants to store a very large integer safely in JavaScript. Which value uses the appropriate modern type?",
        "options": [
            "A) \"12345678901234567890\"",
            "B) 12345678901234567890n",
            "C) Symbol(\"12345678901234567890\")",
            "D) { number: 12345678901234567890 }"
        ],
        "answer": "B",
        "reason": "BigInt values are written by adding n to the end of an integer. BigInt is used for integers too large to be safely represented by the normal Number type."
    },
    {
        "question": "What will be printed? console.log(typeof null);",
        "options": [
            "A) \"null\"",
            "B) \"undefined\"",
            "C) \"object\"",
            "D) \"boolean\""
        ],
        "answer": "C",
        "reason": "In JavaScript, typeof null returns \"object\". This is a long-standing JavaScript behavior, even though null represents the intentional absence of a value."
    },
    {
        "question": "What will be printed? console.log(5 === \"5\");",
        "options": [
            "A) true",
            "B) false",
            "C) \"5\"",
            "D) NaN"
        ],
        "answer": "B",
        "reason": "The strict equality operator === compares both value and type. 5 is a number, while \"5\" is a string, so the result is false."
    },
    {
        "question": "What will be printed? console.log(\"10\" - 4);",
        "options": [
            "A) \"104\"",
            "B) 6",
            "C) \"6\"",
            "D) NaN"
        ],
        "answer": "B",
        "reason": "With the minus operator, JavaScript converts the string \"10\" into the number 10. Then it calculates 10 - 4, which gives 6."
    },
    {
        "question": "What will be printed? console.log(\"10\" + 4);",
        "options": [
            "A) 14",
            "B) \"104\"",
            "C) 6",
            "D) NaN"
        ],
        "answer": "B",
        "reason": "With the plus operator, if one operand is a string, JavaScript performs string concatenation. Therefore, \"10\" + 4 becomes \"104\"."
    },
    {
        "question": "A student wants to check whether a value is really NaN. Which expression is the best choice?",
        "options": [
            "A) value === NaN",
            "B) value == NaN",
            "C) Object.is(value, NaN)",
            "D) typeof value === NaN"
        ],
        "answer": "C",
        "reason": "NaN is unusual because it is not equal to itself using == or ===. Object.is(value, NaN) correctly checks whether the value is actually NaN."
    },
    {
        "question": "What will be printed? const user = {}; console.log(user.profile?.email);",
        "options": [
            "A) null",
            "B) undefined",
            "C) false",
            "D) ReferenceError"
        ],
        "answer": "B",
        "reason": "The optional chaining operator ?. safely stops if profile does not exist. Instead of causing an error, the expression returns undefined."
    },
    {
        "question": "What will be printed? const pageSize = 0; console.log(pageSize ?? 20);",
        "options": [
            "A) 20",
            "B) 0",
            "C) null",
            "D) undefined"
        ],
        "answer": "B",
        "reason": "The nullish coalescing operator ?? only uses the right-side value when the left side is null or undefined. Since 0 is a valid value, 0 is printed."
    },
    {
        "question": "What will be printed? const name = \"Sam\"; console.log(`Hello, ${name}`);",
        "options": [
            "A) Hello, name",
            "B) Hello, Sam",
            "C) Hello, ${name}",
            "D) Hello + Sam"
        ],
        "answer": "B",
        "reason": "Template literals use ${} to insert variable values into a string. Since name is \"Sam\", the output is Hello, Sam."
    },
    {
        "question": "What will be printed? console.log(square(5)); function square(x) { return x * x; }",
        "options": [
            "A) 5",
            "B) 25",
            "C) undefined",
            "D) ReferenceError"
        ],
        "answer": "B",
        "reason": "Function declarations are hoisted, so square can be called before it appears in the code. square(5) returns 5 * 5, which is 25."
    },
    {
        "question": "What will be printed? const double = x => x * 2; console.log(double(7));",
        "options": [
            "A) 7",
            "B) 14",
            "C) undefined",
            "D) x * 2"
        ],
        "answer": "B",
        "reason": "The arrow function takes x and returns x * 2. Passing 7 gives 7 * 2, so the output is 14."
    },
    {
        "question": "What concept is demonstrated by this code? function makeCounter() { let count = 0; return function () { count++; return count; }; } const next = makeCounter(); console.log(next()); console.log(next());",
        "options": [
            "A) Inheritance",
            "B) Destructuring",
            "C) Closure",
            "D) JSON parsing"
        ],
        "answer": "C",
        "reason": "This demonstrates a closure because the returned inner function remembers and continues to access the count variable from makeCounter even after makeCounter has finished running."
    },
    {
        "question": "What will be printed? function countValues(...values) { return values.length; } console.log(countValues(2, 4, 6, 8));",
        "options": [
            "A) 2",
            "B) 8",
            "C) 4",
            "D) 20"
        ],
        "answer": "C",
        "reason": "The rest parameter ...values collects all arguments into an array. Four values are passed, so values.length is 4."
    },
    {
        "question": "What will be printed? const nums = [3, 8, 2]; console.log(Math.max(...nums));",
        "options": [
            "A) [3, 8, 2]",
            "B) 3",
            "C) 8",
            "D) undefined"
        ],
        "answer": "C",
        "reason": "The spread operator ... expands the array into separate arguments. Math.max(3, 8, 2) returns the largest number, which is 8."
    },
    {
        "question": "What will be printed? const a = { value: 10 }; const b = a; b.value = 50; console.log(a.value);",
        "options": [
            "A) 10",
            "B) 50",
            "C) undefined",
            "D) ReferenceError"
        ],
        "answer": "B",
        "reason": "Objects are assigned by reference. a and b point to the same object, so changing b.value also changes a.value."
    },
    {
        "question": "What will be printed? const user = { name: \"Ada\" }; const copy = { ...user, city: \"Ottawa\" }; console.log(copy.name);",
        "options": [
            "A) Ottawa",
            "B) Ada",
            "C) undefined",
            "D) city"
        ],
        "answer": "B",
        "reason": "The object spread operator copies the properties from user into copy. Since user has name: \"Ada\", copy.name is \"Ada\"."
    },
    {
        "question": "What will be printed? const nums = [1, 2, 3]; const result = nums.map(n => n * 10); console.log(result);",
        "options": [
            "A) [1, 2, 3]",
            "B) [10, 20, 30]",
            "C) 60",
            "D) [2, 4, 6]"
        ],
        "answer": "B",
        "reason": "map() creates a new array by applying a function to each element. Each number is multiplied by 10, giving [10, 20, 30]."
    },
    {
        "question": "What will be printed? const nums = [1, 2, 3, 4]; const result = nums.filter(n => n % 2 === 0); console.log(result);",
        "options": [
            "A) [1, 3]",
            "B) [2, 4]",
            "C) [1, 2, 3, 4]",
            "D) 10"
        ],
        "answer": "B",
        "reason": "filter() creates a new array containing only the elements that pass the test. The even numbers are 2 and 4, so the result is [2, 4]."
    },
    {
        "question": "What will be printed? const nums = [5, 10, 15]; const total = nums.reduce((sum, n) => sum + n, 2); console.log(total);",
        "options": [
            "A) 30",
            "B) 32",
            "C) 17",
            "D) 2"
        ],
        "answer": "B",
        "reason": "reduce() starts with the initial value 2, then adds 5, 10, and 15. The total is 2 + 5 + 10 + 15 = 32."
    },
    {
        "question": "What will be printed? const letters = [\"a\", \"b\", \"c\"]; console.log(letters.at(-1));",
        "options": [
            "A) \"a\"",
            "B) \"b\"",
            "C) \"c\"",
            "D) -1"
        ],
        "answer": "C",
        "reason": "The at() method supports negative indexes. at(-1) returns the last element of the array, which is \"c\"."
    },
    {
        "question": "What will happen in this code? class Account { #balance = 0; deposit(amount) { this.#balance += amount; } } const acc = new Account(); console.log(acc.#balance);",
        "options": [
            "A) 0 will be printed",
            "B) undefined will be printed",
            "C) A syntax error will occur",
            "D) The balance will become global"
        ],
        "answer": "C",
        "reason": "#balance is a private class field. It can only be accessed inside the class body, so trying to read acc.#balance outside the class causes a syntax error."
    },
    {
        "question": "What will be printed? const tags = new Set([\"js\", \"html\", \"js\", \"css\"]); console.log(tags.size);",
        "options": [
            "A) 2",
            "B) 3",
            "C) 4",
            "D) 0"
        ],
        "answer": "B",
        "reason": "A Set stores only unique values. The duplicate \"js\" is counted once, so the Set contains js, html, and css, making the size 3."
    },
    {
        "question": "What will be printed? const scores = new Map(); scores.set(\"Ali\", 75); scores.set(\"Sara\", 88); scores.set(\"Ali\", 95); console.log(scores.get(\"Ali\")); console.log(scores.size);",
        "options": [
            "A) 75 and 3",
            "B) 95 and 3",
            "C) 95 and 2",
            "D) undefined and 2"
        ],
        "answer": "C",
        "reason": "A Map stores unique keys. Setting \"Ali\" again updates the existing value from 75 to 95, so get(\"Ali\") returns 95 and the map size is 2."
    },
    {
        "question": "In the following code, which message is printed first? async function loadData() { await fetch(\"/api/data\"); console.log(\"data loaded\"); } loadData(); console.log(\"request sent\");",
        "options": [
            "A) \"data loaded\"",
            "B) \"request sent\"",
            "C) Both messages print at the same time",
            "D) Nothing is printed because fetch is invalid"
        ],
        "answer": "B",
        "reason": "The await pauses the async function until fetch finishes, but the rest of the program continues running. Therefore, \"request sent\" prints before \"data loaded\"."
    },
    {
        "question": "What will be printed? const grades = new Map(); grades.set(\"Maya\", 85); grades.set(\"Omar\", 92); grades.set(\"Maya\", 90); console.log(grades.get(\"Maya\")); console.log(grades.size);",
        "options": [
            "A) 85 and 3",
            "B) 90 and 3",
            "C) 90 and 2",
            "D) undefined and 2"
        ],
        "answer": "C",
        "reason": "Map keys are unique. Setting the key \"Maya\" a second time updates the existing value to 90 instead of adding a new entry, so the size remains 2."
    }
]