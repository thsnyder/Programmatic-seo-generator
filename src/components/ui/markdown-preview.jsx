import React from 'react'
import ReactMarkdown from 'react-markdown'

export function MarkdownPreview({ content, className = '' }) {
  return (
    <div className={`prose prose-lg max-w-none ${className}`}>
      <ReactMarkdown
        components={{
          h1: ({ children }) => (
            <h1 className="text-3xl font-bold text-files-headline-black mb-4 border-b border-files-light-pink pb-2">
              {children}
            </h1>
          ),
          h2: ({ children }) => (
            <h2 className="text-2xl font-semibold text-files-headline-black mt-8 mb-4">
              {children}
            </h2>
          ),
          h3: ({ children }) => (
            <h3 className="text-xl font-semibold text-files-headline-black mt-6 mb-3">
              {children}
            </h3>
          ),
          p: ({ children }) => (
            <p className="text-files-headline-black/80 leading-relaxed mb-4">
              {children}
            </p>
          ),
          ul: ({ children }) => (
            <ul className="list-disc list-inside text-files-headline-black/80 mb-4 space-y-1">
              {children}
            </ul>
          ),
          ol: ({ children }) => (
            <ol className="list-decimal list-inside text-files-headline-black/80 mb-4 space-y-1">
              {children}
            </ol>
          ),
          li: ({ children }) => (
            <li className="text-files-headline-black/80">
              {children}
            </li>
          ),
          strong: ({ children }) => (
            <strong className="font-semibold text-files-primary-red">
              {children}
            </strong>
          ),
          em: ({ children }) => (
            <em className="italic text-files-maroon">
              {children}
            </em>
          ),
          blockquote: ({ children }) => (
            <blockquote className="border-l-4 border-files-primary-red pl-4 py-2 bg-files-light-pink/20 italic text-files-headline-black/70 mb-4">
              {children}
            </blockquote>
          ),
          code: ({ children, className }) => {
            const isInline = !className
            if (isInline) {
              return (
                <code className="bg-files-light-pink px-1.5 py-0.5 rounded text-files-primary-red text-sm font-mono">
                  {children}
                </code>
              )
            }
            return (
              <pre className="bg-files-light-gray p-4 rounded-lg overflow-x-auto mb-4">
                <code className="text-files-headline-black text-sm font-mono">
                  {children}
                </code>
              </pre>
            )
          },
          a: ({ children, href }) => (
            <a 
              href={href} 
              className="text-files-primary-red hover:text-files-bright-red underline"
              target="_blank"
              rel="noopener noreferrer"
            >
              {children}
            </a>
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
} 